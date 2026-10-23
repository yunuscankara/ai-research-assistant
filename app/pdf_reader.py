from pathlib import Path

from pypdf import PdfReader


def extract_pages_from_pdf(file_path: str) -> list[dict]:
    """Extract text from a PDF while preserving page numbers."""

    pdf_path = Path(file_path)

    if not pdf_path.exists():
        raise FileNotFoundError(
            f"PDF file not found: {pdf_path.resolve()}"
        )

    reader = PdfReader(str(pdf_path))

    extracted_pages = []

    for page_number, page in enumerate(reader.pages, start=1):
        page_text = (page.extract_text() or "").strip()

        if page_text:
            extracted_pages.append(
                {
                    "page_number": page_number,
                    "text": page_text,
                }
            )

    if not extracted_pages:
        raise ValueError(
            "No extractable text found in the PDF. "
            "The document may require OCR."
        )

    return extracted_pages