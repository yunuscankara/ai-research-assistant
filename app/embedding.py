from sentence_transformers import SentenceTransformer


MODEL_NAME = "paraphrase-multilingual-MiniLM-L12-v2"


def load_embedding_model() -> SentenceTransformer:
    """Load the multilingual embedding model."""
    return SentenceTransformer(MODEL_NAME)


def generate_embeddings(
    texts: list[str],
    model: SentenceTransformer
):
    """Convert text chunks into numerical vectors."""
    embeddings = model.encode(
        texts,
        normalize_embeddings=True
    )

    return embeddings