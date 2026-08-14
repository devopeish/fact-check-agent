from fact_checker import fact_check_pdf


PDF_PATH = "test.pdf"


def show_progress(message):
    print(
        f"[INFO] {message}"
    )


print(
    "\nStarting full fact-check pipeline...\n"
)


with open(
    PDF_PATH,
    "rb"
) as file:

    pdf_bytes = file.read()


result = fact_check_pdf(
    pdf_bytes,
    progress_callback=show_progress,
    max_claims=2
)


print(
    "\n"
    + "=" * 80
)

print(
    "FINAL RESULTS"
)

print(
    "=" * 80
)


print(
    f"Pages processed: "
    f"{len(result['pages'])}"
)

print(
    f"Claims extracted: "
    f"{len(result['claims'])}"
)

print(
    f"Claims verified: "
    f"{len(result['results'])}"
)


for item in result["results"]:

    print(
        "\n"
        + "-" * 80
    )

    print(
        f"Page {item.get('page')} "
        f"| {item.get('verdict')} "
        f"| {item.get('confidence')}"
    )

    print(
        item.get(
            "claim",
            ""
        )
    )

    print(
        f"\nReason: "
        f"{item.get('reason', '')}"
    )