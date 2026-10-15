# AI Research Assistant

A Retrieval-Augmented Generation (RAG) application that answers questions about PDF documents using semantic search, vector embeddings, and a locally running Large Language Model (LLM).

This project combines document processing, semantic retrieval, and local AI inference to generate answers based on information retrieved from PDF documents.

## Features

- Extracts text from PDF documents
- Splits long documents into smaller text chunks
- Generates text embeddings using Sentence Transformers
- Stores document embeddings in ChromaDB
- Retrieves relevant document sections using semantic search
- Generates answers using Ollama and Qwen2.5:3b
- Accepts user questions through an interactive terminal interface
- Uses retrieved document content to provide context-based answers
- Runs the language model locally through Ollama

## Tech Stack

- **Language:** Python
- **PDF Processing:** PyMuPDF, pypdf
- **Text Embeddings:** Sentence Transformers
- **Vector Database:** ChromaDB
- **LLM Runtime:** Ollama
- **Language Model:** Qwen2.5:3b
- **HTTP Requests:** Requests

## How It Works

The application follows a basic Retrieval-Augmented Generation (RAG) pipeline.

1. **PDF Text Extraction:** Extracts text from the selected PDF document.
2. **Text Chunking:** Splits the extracted text into smaller chunks.
3. **Embedding Generation:** Converts text chunks into numerical vector representations.
4. **Vector Storage:** Stores the chunks and their embeddings in ChromaDB.
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

Before running the application, make sure you have the following installed:

- Python 3.10 or later
- pip
- Ollama
- Qwen2.5:3b model

You will also need a PDF document containing extractable text.

## Installation

### 1. Clone the Repository

Replace the repository URL with the URL of your GitHub repository.

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
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

Place your PDF file inside the `data/` directory.

For example:

```text
data/sample.pdf
```

The current application uses the following PDF path:

```python
pdf_path = "data/sample.pdf"
```

If your PDF has a different filename, update the path in `main.py`.

### 2. Run the Application

Activate your virtual environment and execute:

```bash
python main.py
```

### 3. Ask a Question

When prompted, enter a question about the document.

Example:

```text
Sorunuzu yazın: Sınav kaç sorudan oluşuyor?
```

The application will retrieve relevant text chunks and generate an answer based on the retrieved context.

## Example

**Question:**

```text
Yazılı sınav toplam kaç sorudan oluşuyor ve kaç dakika sürüyor?
```

**Answer:**

```text
Yazılı sınav toplam 140 sorudan oluşmaktadır ve toplam 160 dakikadır sürecektir.
```

The answer is generated using information retrieved from the source PDF.

*Note: This example is based on the PDF used during development. Your results will depend on the document you provide.*

## Configuration

### Embedding Model

The project uses the following Sentence Transformers model:

```text
paraphrase-multilingual-MiniLM-L12-v2
```

This model generates multilingual text embeddings for semantic search.

### Language Model

The application uses:

```text
qwen2.5:3b
```

The model runs locally through Ollama.

### Vector Database

ChromaDB stores the document chunks and their embeddings for similarity-based retrieval.

## Current Limitations

- The application currently processes a PDF using a configured file path.
- Text chunking is based on character length.
- Retrieval quality depends on the embedding model and chunking strategy.
- Generated answers may be inaccurate or incomplete.
- Scanned PDFs may require OCR if they do not contain extractable text.
- The current implementation is designed for terminal-based interaction.

## Future Improvements

- Support multiple PDF documents
- Improve text chunking strategies
- Store document names and page numbers as metadata
- Improve retrieval quality through retrieval evaluation
- Add conversation history
- Add answer citations and source page references
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

## Disclaimer

The generated answers depend on the quality of the source document and the relevance of the retrieved text chunks. Always verify important information against the original document.

## Author

**Yunus Cankara**

GitHub: [yunuscankara](https://github.com/yunuscankara)