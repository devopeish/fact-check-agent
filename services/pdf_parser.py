import fitz


def extract_pdf_pages(pdf_bytes):
    """
    Extract readable text from every page of a PDF.

    Returns:
        [
            {
                "page": 1,
                "text": "..."
            },
            ...
        ]
    """

    document = fitz.open(
        stream=pdf_bytes,
        filetype="pdf"
    )

    pages = []

    try:

        for page_number, page in enumerate(
            document,
            start=1
        ):

            text = page.get_text("text").strip()

            if text:
                pages.append({
                    "page": page_number,
                    "text": text
                })

    finally:

        document.close()

    return pages