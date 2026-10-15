from app.pdf_reader import extract_text_from_pdf
from app.chunker import split_text_into_chunks
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
    text = extract_text_from_pdf(pdf_path)

    print("Total characters:", len(text))

    chunks = split_text_into_chunks(
        text,
        chunk_size=500,
        overlap=50,
    )

    print("Total chunks:", len(chunks))

    if not chunks:
        print("No text chunks were generated from the PDF.")
        return

    print("\nLoading embedding model...")
    model = load_embedding_model()

    print("\nGenerating document embeddings...")
    embeddings = generate_embeddings(chunks, model)

    print("Embedding shape:", embeddings.shape)

    print("\nSaving chunks to ChromaDB...")
    collection = create_vector_store()

    add_chunks_to_store(
        chunks,
        embeddings,
        collection,
    )

    query = input("\nSorunuzu yazın: ")

    print("\nQuestion:", query)

    query_embedding = generate_embeddings(
        [query],
        model,
    )[0]

    print("\nSearching for relevant document chunks...")

    results = search_similar_chunks(
        query_embedding,
        collection,
        n_results=min(3, len(chunks)),
    )

    retrieved_documents = results["documents"][0]

    if not retrieved_documents:
        print("No relevant document chunks were found.")
        return

    print("\nRelevant document chunks:")

    for index, document in enumerate(retrieved_documents, start=1):
        print(f"\n--- Result {index} ---")
        print(document)

    context = "\n\n".join(retrieved_documents)

    print("\nGenerating answer with Qwen2.5:3b...")

    answer = generate_answer(
        question=query,
        context=context,
    )

    print("\n" + "=" * 50)
    print("AI RESEARCH ASSISTANT ANSWER")
    print("=" * 50)

    print(answer)

    print("\n" + "=" * 50)


if __name__ == "__main__":
    main()