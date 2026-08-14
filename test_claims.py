from services.pdf_parser import extract_pdf_pages
from agents.claim_extractor import extract_claims


# Read PDF
with open("test.pdf", "rb") as file:
    pdf_bytes = file.read()


# Extract pages
pages = extract_pdf_pages(pdf_bytes)

print(f"\nExtracted {len(pages)} pages.")


# Extract factual claims
claims = extract_claims(pages)

print(f"\nFound {len(claims)} factual claims.\n")


for claim in claims:
    print("=" * 70)
    print(f"Claim ID   : {claim['claim_id']}")
    print(f"Page       : {claim['page']}")
    print(f"Type       : {claim['claim_type']}")
    print(f"Claim      : {claim['claim']}")