import pymupdf

pdf_path = "data/sample.pdf"

doc = pymupdf.open(pdf_path)

print("Total pages:", len(doc))

for page_number, page in enumerate(doc, start=1):
    text = page.get_text()

    print(f"\n{'=' * 50}")
    print(f"PAGE {page_number}")
    print("=" * 50)

    print(text[:1500])

doc.close()