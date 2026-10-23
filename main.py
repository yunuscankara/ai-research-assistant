from app.pdf_reader import extract_pages_from_pdf
from app.chunker import split_pages_into_chunks
from app.embedding import load_embedding_model, generate_embeddings
from app.llm import generate_answer
from app.vector_store import (
    create_vector_store,
    add_chunks_to_store,
    search_similar_chunks,
)

def main():
    pdf_path = "data/sample.pdf"

    print("Reading PDF document...")
    pages = extract_pages_from_pdf(pdf_path)

    total_characters = sum(len(page["text"]) for page in pages)
    print("Total pages with extractable text:", len(pages))
    print("Total characters:", total_characters)

    chunks = split_pages_into_chunks(
        pages,
        chunk_size=800,
        overlap=100,
    )

    print("Total chunks:", len(chunks))

    if not chunks:
        print("No text chunks were generated from the PDF.")
        return

    chunk_texts = [chunk["text"] for chunk in chunks]

    print("\nLoading embedding model...")
    model = load_embedding_model()

    print("\nGenerating document embeddings...")
    embeddings = generate_embeddings(chunk_texts, model)
    print("Embedding shape:", embeddings.shape)

    print("\nSaving chunks to ChromaDB...")
    collection = create_vector_store()

    add_chunks_to_store(chunks, embeddings, collection)

    query = input("\nSorunuzu yazın: ").strip()

    if not query:
        print("Please enter a question.")
        return

    print("\nQuestion:", query)

    query_embedding = generate_embeddings([query], model)[0]

    print("\nSearching for relevant document chunks...")
    results = search_similar_chunks(
        query_embedding,
        collection,
        n_results=5,
    )

    retrieved_documents = results["documents"][0]
    retrieved_metadata = results["metadatas"][0]

    if not retrieved_documents:
        print("No relevant document chunks were found.")
        return

    print("\nRelevant document chunks:")

    for index, document in enumerate(retrieved_documents, start=1):
        metadata = retrieved_metadata[index - 1]
        page_number = metadata.get("page_number", "Unknown")

        print(f"\n--- Result {index} | Page {page_number} ---")
        print(document)

    context_parts = []

    for document, metadata in zip(
        retrieved_documents,
        retrieved_metadata,
    ):
        page_number = metadata.get("page_number", "Unknown")
        context_parts.append(
            f"\n{document}"
        )

    context = "\n\n".join(context_parts)

    print("\nGenerating answer with Qwen2.5:3b...")
    answer = generate_answer(question=query, context=context)

    source_pages = sorted(
        {
            metadata["page_number"]
            for metadata in retrieved_metadata
            if metadata.get("page_number") is not None
        }
    )

    print("\n" + "=" * 50)
    print("AI RESEARCH ASSISTANT ANSWER")
    print("=" * 50)
    print(answer)

    print("\nSources:")

    if source_pages:
        for page_number in source_pages:
            print(f"- {pdf_path}, page {page_number}")
    else:
        print("- Source page information is unavailable.")

    print("=" * 50)

if __name__ == "__main__":
    main()