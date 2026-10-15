import chromadb


def create_vector_store():
    

    client = chromadb.PersistentClient(
        path="./chroma_db"
    )

    collection = client.get_or_create_collection(
        name="research_documents",
        metadata={"hnsw:space": "cosine"}
    )

    return collection


def add_chunks_to_store(chunks, embeddings, collection):
    

    collection.upsert(
        ids=[f"chunk_{i}" for i in range(len(chunks))],
        documents=chunks,
        embeddings=embeddings.tolist(),
        metadatas=[
            {"chunk_index": i}
            for i in range(len(chunks))
        ]
    )

    print(f"Stored {len(chunks)} chunks in ChromaDB.")

def search_similar_chunks(query_embedding, collection, n_results=3):
   

    results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=n_results
    )

    return results