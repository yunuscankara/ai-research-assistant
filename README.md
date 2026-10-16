# AI Research Assistant

A Retrieval-Augmented Generation (RAG) application that answers questions about PDF documents using semantic search, vector embeddings, and a locally running Large Language Model (LLM).

The project combines document processing, semantic retrieval, and local AI inference to generate answers based on information retrieved from PDF documents.

## Features

- Extracts text from PDF documents
- Splits long documents into smaller text chunks
- Generates text embeddings using Sentence Transformers
- Stores document embeddings in ChromaDB
- Retrieves relevant document sections using semantic search
- Generates answers using Ollama and Qwen2.5:3b
- Accepts user questions through an interactive terminal interface
- Uses retrieved document content to generate context-based answers
- Runs the language model locally through Ollama

## Tech Stack

- **Programming Language:** Python
- **PDF Processing:** PyMuPDF, pypdf
- **Text Embeddings:** Sentence Transformers
- **Vector Database:** ChromaDB
- **LLM Runtime:** Ollama
- **Language Model:** Qwen2.5:3b
- **HTTP Communication:** Requests

## How It Works

The application follows a basic Retrieval-Augmented Generation (RAG) pipeline.

1. **PDF Text Extraction:** Extracts text from the selected PDF document.
2. **Text Chunking:** Splits the extracted text into smaller chunks.
3. **Embedding Generation:** Converts document chunks into numerical vector representations.
4. **Vector Storage:** Stores the text chunks and their embeddings in ChromaDB.
5. **Semantic Search:** Converts the user's question into an embedding and retrieves relevant document chunks.
6. **Context Preparation:** Combines the retrieved chunks into context for the language model.
7. **Answer Generation:** Sends the question and retrieved context to the local Qwen2.5:3b model through Ollama.
8. **Response Display:** Prints the generated answer in the terminal.

## Project Structure

```text
ai-research-assistant/
├── app/
│   ├── __init__.py
│   ├── chunker.py
│   ├── embedding.py
│   ├── llm.py
│   ├── pdf_reader.py
│   └── vector_store.py
├── data/
├── main.py
├── requirements.txt
├── test_pdf.py
├── .gitignore
└── README.md
```

## Requirements

Before running the application, make sure you have:

- Python 3.10 or later
- pip
- Ollama
- The Qwen2.5:3b model
- A PDF document containing extractable text

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yunuscankara/ai-research-assistant.git
cd ai-research-assistant
```

### 2. Create a Virtual Environment

```bash
python3 -m venv .venv
```

Activate the virtual environment on macOS or Linux:

```bash
source .venv/bin/activate
```

### 3. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### 4. Set Up Ollama

Install Ollama if it is not already installed.

Download the Qwen2.5:3b model:

```bash
ollama pull qwen2.5:3b
```

Make sure the Ollama service is running before starting the application.

## Usage

### 1. Add a PDF Document

Place your PDF document inside the `data/` directory.

The current application expects the following file path:

```text
data/sample.pdf
```

Make sure your PDF file is named `sample.pdf` or update the `pdf_path` variable in `main.py` to match your filename.

The application requires a PDF containing extractable text. Scanned documents may require OCR before their text can be processed.

### 2. Run the Application

Activate your virtual environment and run:

```bash
python main.py
```

The application will extract the PDF text, split it into chunks, generate embeddings, and store them in ChromaDB before accepting a question.

### 3. Ask a Question

Enter your question when prompted by the terminal.

Example:

```text
Sorunuzu yazın: Sınav kaç sorudan oluşuyor?
```

The application retrieves relevant text chunks from the document and generates an answer using the local language model.

## Example

**Question:**

```text
Yazılı sınav toplam kaç sorudan oluşuyor ve kaç dakika sürüyor?
```

**Answer:**

```text
Yazılı sınav toplam 140 sorudan oluşmaktadır ve toplam 160 dakikadır sürecektir.
```

This example is based on the PDF document used during development. Results depend on the document provided and the relevance of the retrieved text chunks.

## Configuration

### Embedding Model

The project uses the following Sentence Transformers model:

```text
paraphrase-multilingual-MiniLM-L12-v2
```

The model generates multilingual text embeddings for semantic search.

### Language Model

The application uses:

```text
qwen2.5:3b
```

The model runs locally through Ollama.

### Vector Database

ChromaDB stores document chunks and their embeddings for similarity-based retrieval.

The current implementation uses a persistent local ChromaDB database.

## Current Limitations

- The application currently processes a PDF using a configured file path.
- Text chunking is based on character length.
- Retrieval quality depends on the embedding model and chunking strategy.
- Generated answers may be inaccurate or incomplete.
- Scanned PDFs may require OCR.
- The current implementation is designed for terminal-based interaction.
- Document metadata and source page references can be improved.
- The current vector-store implementation needs improvements before reliably supporting multiple documents.

## Future Improvements

- Support multiple PDF documents
- Improve text chunking strategies
- Store document names and page numbers as metadata
- Improve retrieval quality through systematic evaluation
- Add source page references to generated answers
- Add conversation history
- Build a web interface using FastAPI
- Add automated tests
- Improve error handling and input validation

## Learning Objectives

This project provides practical experience with:

- Retrieval-Augmented Generation (RAG)
- Text embeddings and vector representations
- Semantic search
- Vector databases
- PDF document processing
- Local Large Language Models
- REST API communication
- Python application structure
- Integrating an LLM into a Python application

## Disclaimer

The generated answers depend on the quality of the source document and the relevance of the retrieved text chunks. The model may generate inaccurate or incomplete answers. Always verify important information against the original document.

## Author

**Yunus Cankara**

GitHub: https://github.com/yunuscankara