import chromadb


def create_vector_store():
    client = chromadb.PersistentClient(
        path="./chroma_db"
    )

    collection = client.get_or_create_collection(
        name="research_documents",
        metadata={"hnsw:space": "cosine"},
    )

    return collection


def add_chunks_to_store(chunks, embeddings, collection):
    if not chunks:
        raise ValueError("Cannot store empty chunks.")

    if len(chunks) != len(embeddings):
        raise ValueError(
            "The number of chunks must match the number of embeddings."
        )

    existing_ids = collection.get()["ids"]

    if existing_ids:
        collection.delete(ids=existing_ids)

    collection.upsert(
        ids=[f"chunk_{i}" for i in range(len(chunks))],
        documents=[chunk["text"] for chunk in chunks],
        embeddings=embeddings.tolist(),
        metadatas=[
            {
                "chunk_index": i,
                "page_number": chunk["page_number"],
                "source": "sample.pdf",
            }
            for i, chunk in enumerate(chunks)
        ],
    )

    print(f"Stored {len(chunks)} chunks in ChromaDB.")


def search_similar_chunks(
    query_embedding,
    collection,
    n_results=5,
):
    collection_count = collection.count()

    if collection_count == 0:
        return {
            "documents": [[]],
            "ids": [[]],
            "metadatas": [[]],
            "distances": [[]],
        }

    return collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=min(n_results, collection_count),
    )