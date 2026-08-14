from services.web_search import search_web


claim = (
    "Data Analytics can be divided into four major types: "
    "Descriptive, Diagnostic, Predictive, and Prescriptive."
)


print("\nSearching live web...\n")

results = search_web(claim, max_results=5)


print(f"Found {len(results)} sources.\n")


for index, result in enumerate(results, start=1):

    print("=" * 80)

    print(f"SOURCE {index}")

    print("=" * 80)

    print(f"Title: {result['title']}")

    print(f"URL: {result['url']}")

    print(f"Score: {result['score']}")

    print("\nEvidence:")

    print(result["content"][:1000])

    print()