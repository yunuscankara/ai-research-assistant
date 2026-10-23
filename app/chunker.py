import re


def split_text_into_chunks(
    text: str,
    chunk_size: int = 800,
    overlap: int = 100,
) -> list[str]:
    """Split text into overlapping chunks while preserving sentence boundaries."""

    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than 0")

    if overlap < 0:
        raise ValueError("overlap cannot be negative")

    if overlap >= chunk_size:
        raise ValueError("overlap must be smaller than chunk_size")

    text = text.strip()

    if not text:
        return []

    paragraphs = [
        paragraph.strip()
        for paragraph in re.split(r"\n\s*\n", text)
        if paragraph.strip()
    ]

    if not paragraphs:
        paragraphs = [text]

    segments = []

    for paragraph in paragraphs:
        if len(paragraph) <= chunk_size:
            segments.append(paragraph)
            continue

        sentences = re.split(r"(?<=[.!?])\s+", paragraph)

        for sentence in sentences:
            sentence = sentence.strip()

            while len(sentence) > chunk_size:
                segments.append(sentence[:chunk_size].strip())
                sentence = sentence[chunk_size:].strip()

            if sentence:
                segments.append(sentence)

    chunks = []
    current_chunk = ""

    for segment in segments:
        candidate = (
            f"{current_chunk}\n{segment}"
            if current_chunk
            else segment
        )

        if len(candidate) <= chunk_size:
            current_chunk = candidate
        else:
            chunks.append(current_chunk.strip())
            current_chunk = segment

    if current_chunk:
        chunks.append(current_chunk.strip())

    if overlap == 0 or len(chunks) <= 1:
        return chunks

    overlapped_chunks = [chunks[0]]

    for chunk in chunks[1:]:
        previous_chunk = overlapped_chunks[-1]
        overlap_text = previous_chunk[-overlap:]

        overlapped_chunks.append(
            f"{overlap_text}\n{chunk}".strip()
        )

    return overlapped_chunks


def split_pages_into_chunks(
    pages: list[dict],
    chunk_size: int = 800,
    overlap: int = 100,
) -> list[dict]:
    """Split PDF pages into chunks while preserving page metadata."""

    all_chunks = []

    for page in pages:
        page_chunks = split_text_into_chunks(
            page["text"],
            chunk_size=chunk_size,
            overlap=overlap,
        )

        for chunk in page_chunks:
            all_chunks.append(
                {
                    "text": chunk,
                    "page_number": page["page_number"],
                }
            )

    return all_chunks