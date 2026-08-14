from services.pdf_parser import extract_pdf_pages


with open("test.pdf", "rb") as file:
    pdf_bytes = file.read()


pages = extract_pdf_pages(pdf_bytes)


print(f"\nTotal pages extracted: {len(pages)}")

for page in pages:
    print("\n" + "=" * 60)
    print(f"PAGE {page['page']}")
    print("=" * 60)
    print(page["text"][:1000])