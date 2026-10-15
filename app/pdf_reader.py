from pathlib import Path

from pypdf import PdfReader


def extract_text_from_pdf(file_path: str) -> str:
    """Extract text from a PDF file."""

    pdf_path = Path(file_path)

    # Check whether the PDF file exists
    if not pdf_path.exists():
        raise FileNotFoundError(
            f"PDF file not found: {pdf_path.resolve()}"
        )

    # Open the PDF file
    reader = PdfReader(str(pdf_path))

    extracted_pages = []

    # Extract text from each page
    for page_number, page in enumerate(reader.pages, start=1):
        page_text = page.extract_text() or ""

        extracted_pages.append(
            f"[Page {page_number}]\n{page_text}"
        )

    # Combine all pages into a single string
    return "\n\n".join(extracted_pages)