from services.pdf_parser import extract_pdf_pages
from agents.claim_extractor import extract_claims
from agents.verifier import verify_claim


def fact_check_pdf(
    pdf_bytes,
    progress_callback=None,
    max_claims=None
):
    """
    Complete PDF fact-checking pipeline.

    PDF
      ↓
    Extract pages
      ↓
    Extract claims
      ↓
    Optionally limit claims for testing
      ↓
    Verify claims
      ↓
    Return results
    """


    # ========================================================
    # STEP 1: Extract PDF pages
    # ========================================================

    if progress_callback:

        progress_callback(
            "Reading PDF..."
        )

    pages = extract_pdf_pages(
        pdf_bytes
    )


    if not pages:

        raise ValueError(
            "No readable text was found in the PDF."
        )


    # ========================================================
    # STEP 2: Extract claims
    # ========================================================

    if progress_callback:

        progress_callback(
            "Extracting factual claims with Gemini..."
        )

    claims = extract_claims(
        pages
    )


    # ========================================================
    # Optional testing limit
    # ========================================================

    if max_claims is not None:

        claims = claims[
            :max_claims
        ]


    if not claims:

        return {
            "pages": pages,
            "claims": [],
            "results": []
        }


    # ========================================================
    # STEP 3: Verify claims
    # ========================================================

    results = []

    total_claims = len(
        claims
    )


    for index, claim in enumerate(
        claims,
        start=1
    ):

        if progress_callback:

            progress_callback(
                f"Verifying claim "
                f"{index} of {total_claims}..."
            )


        try:

            result = verify_claim(
                claim
            )

            results.append(
                result
            )


        except Exception as error:

            results.append({

                "claim": claim.get(
                    "claim",
                    ""
                ),

                "page": claim.get(
                    "page"
                ),

                "verdict": "ERROR",

                "confidence": 0.0,

                "reason": (
                    f"Verification failed: "
                    f"{str(error)}"
                ),

                "correct_fact": "",

                "sources": []

            })


    # ========================================================
    # STEP 4: Return everything
    # ========================================================

    return {

        "pages": pages,

        "claims": claims,

        "results": results

    }