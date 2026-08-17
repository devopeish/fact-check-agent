import streamlit as st
from fact_checker import fact_check_pdf

# Page Configuration

st.set_page_config(
    page_title="Fact-Check Agent",
    page_icon="🔎",
    layout="centered"
)

# Header

st.title("🔎 Fact-Check Agent")

st.markdown(
    """
    Upload a PDF and the Fact-Check Agent will:

    1. Extract factual claims
    2. Search the live web for evidence
    3. Verify each claim using Gemini
    4. Display the verdict with supporting sources
    """
)

# File Upload

uploaded_file = st.file_uploader(
    "Upload a PDF",
    type=["pdf"]
)

# Fact Check

if uploaded_file:

    st.success(
        f"Uploaded: {uploaded_file.name}"
    )


    if st.button(
        "🔎 Fact Check PDF",
        type="primary"
    ):

        pdf_bytes = (
            uploaded_file.getvalue()
        )

        progress_placeholder = st.empty()


        def show_progress(message):

            progress_placeholder.info(
                message
            )


        try:

            with st.spinner(
                "Analyzing your document..."
            ):

                # PRODUCTION MODE
                # No claim limit.

                result = fact_check_pdf(
                    pdf_bytes,
                    progress_callback=show_progress
                )


            progress_placeholder.success(
                "Fact-checking completed!"
            )


            # Results

            results = result.get(
                "results",
                []
            )

            total = len(
                results
            )


            verified = sum(
                1
                for item in results
                if item.get("verdict")
                == "VERIFIED"
            )


            inaccurate = sum(
                1
                for item in results
                if item.get("verdict")
                == "INACCURATE"
            )


            false = sum(
                1
                for item in results
                if item.get("verdict")
                == "FALSE"
            )


            no_evidence = sum(
                1
                for item in results
                if item.get("verdict")
                == "NO EVIDENCE"
            )


            errors = sum(
                1
                for item in results
                if item.get("verdict")
                == "ERROR"
            )


            # Summary

            st.subheader(
                f"📊 {total} Claims Analyzed"
            )


            col1, col2, col3, col4, col5 = (
                st.columns(5)
            )


            col1.metric(
                "🟢 Verified",
                verified
            )


            col2.metric(
                "🟡 Inaccurate",
                inaccurate
            )


            col3.metric(
                "🔴 False",
                false
            )


            col4.metric(
                "⚪ No Evidence",
                no_evidence
            )


            col5.metric(
                "⚠️ Errors",
                errors
            )


            st.divider()


            # Individual Claims

            st.subheader(
                "📋 Claim Analysis"
            )


            for index, item in enumerate(
                results,
                start=1
            ):

                verdict = item.get(
                    "verdict",
                    "ERROR"
                )


                if verdict == "VERIFIED":

                    icon = "🟢"


                elif verdict == "INACCURATE":

                    icon = "🟡"


                elif verdict == "FALSE":

                    icon = "🔴"


                elif verdict == "NO EVIDENCE":

                    icon = "⚪"


                else:

                    icon = "⚠️"


                page = item.get(
                    "page",
                    "N/A"
                )


                with st.expander(
                    f"{icon} Claim {index} "
                    f"• Page {page} "
                    f"• {verdict}"
                ):


                    st.markdown(
                        "**Claim:**"
                    )


                    st.write(
                        item.get(
                            "claim",
                            "No claim available."
                        )
                    )


                    confidence = item.get(
                        "confidence",
                        0
                    )


                    try:

                        confidence = float(
                            confidence
                        )

                    except (
                        TypeError,
                        ValueError
                    ):

                        confidence = 0


                    confidence = max(
                        0,
                        min(
                            confidence,
                            1
                        )
                    )


                    st.markdown(
                        f"**Confidence:** "
                        f"{confidence:.0%}"
                    )


                    st.markdown(
                        "**Reason:**"
                    )


                    st.write(
                        item.get(
                            "reason",
                            "No reason provided."
                        )
                    )


                    correct_fact = item.get(
                        "correct_fact"
                    )


                    if correct_fact:

                        st.markdown(
                            "**Correct Fact:**"
                        )

                        st.write(
                            correct_fact
                        )


                    sources = item.get(
                        "sources",
                        []
                    )


                    if sources:

                        st.markdown(
                            "**Sources:**"
                        )


                        for source in sources:

                            title = source.get(
                                "title",
                                "Source"
                            )

                            url = source.get(
                                "url",
                                ""
                            )


                            if url:

                                st.markdown(
                                    f"- [{title}]"
                                    f"({url})"
                                )


                    else:

                        st.info(
                            "No supporting "
                            "sources were found."
                        )

        # Error Handling

        except Exception as error:

            error_text = str(
                error
            )


            if (
                "429" in error_text
                or "RESOURCE_EXHAUSTED"
                in error_text
            ):

                st.error(
                    "⚠️ Gemini API quota "
                    "has been reached."
                )

                st.info(
                    "Please try again after "
                    "the Gemini API quota resets."
                )


            elif (
                "503" in error_text
                or "UNAVAILABLE"
                in error_text
            ):

                st.error(
                    "⚠️ Gemini is temporarily "
                    "unavailable."
                )

                st.info(
                    "Please wait a few moments "
                    "and try again."
                )


            elif (
                "No readable text"
                in error_text
            ):

                st.error(
                    "⚠️ The PDF could not "
                    "be read."
                )

                st.info(
                    "Please upload a valid PDF "
                    "containing readable text."
                )


            else:

                st.error(
                    "⚠️ Something went wrong "
                    "while processing the document."
                )

                st.exception(
                    error
                )