import requests


OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL_NAME = "qwen2.5:3b"


def generate_answer(question: str, context: str) -> str:
    """Generate an answer using retrieved document context."""

    messages = [
        {
            "role": "system",
            "content": (
                "You are an AI research assistant. "
                "Answer the user's question using only the "
                "provided document context. "
                "If the context does not contain enough information, "
                "clearly state that the document does not provide "
                "enough information. Answer in Turkish."
            ),
        },
        {
            "role": "user",
            "content": (
                f"Document context:\n{context}\n\n"
                f"Question:\n{question}"
            ),
        },
    ]

    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL_NAME,
                "messages": messages,
                "stream": False,
            },
            timeout=180,
        )

        response.raise_for_status()

        result = response.json()

        return result["message"]["content"]

    except requests.RequestException as error:
        raise RuntimeError(
            f"Could not communicate with Ollama: {error}"
        ) from error