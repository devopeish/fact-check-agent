from agents.verifier import verify_claim


test_claim = {
    "claim": (
        "Data Analytics can be divided into four major types: "
        "Descriptive, Diagnostic, Predictive, and Prescriptive."
    ),
    "page": 2
}


print("\n" + "=" * 80)
print("FACT CHECK TEST")
print("=" * 80)

print("\nClaim:")
print(test_claim["claim"])

print("\nSearching and verifying...")

result = verify_claim(test_claim)


print("\n" + "=" * 80)
print("RESULT")
print("=" * 80)

print(f"\nVerdict    : {result['verdict']}")
print(f"Confidence : {result['confidence']}")
print(f"\nReason:\n{result['reason']}")

print(f"\nCorrect fact:\n{result['correct_fact']}")

print("\nSources:")

for index, source in enumerate(result["sources"], start=1):
    print(f"\n{index}. {source['title']}")
    print(source["url"])