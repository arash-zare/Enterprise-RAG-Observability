# Phase 2: Document Ingestion & Semantic Retrieval

## 🎯 Goal & Overview
The objective of Phase 2 is to build the document ingestion and retrieval pipeline for the Enterprise Local Agentic RAG project.

The pipeline loads documents, extracts their text, divides the text into overlapping chunks, creates an embedding for each chunk using Ollama, and stores the vectors with their source text and metadata in Qdrant. It also embeds a user query and retrieves the most relevant chunks from the collection.

At the end of this phase, the project can search ingested document content by semantic similarity. The retrieved text can then be supplied to an LLM as context for question answering.

---

## 🏗️ Architecture & Component Roles

### 1. Document Loader
- **Role:** Reads supported files from the project’s document directory and returns their text and source information.
- **Initial input focus:** PDF files.
- **Other formats discussed:** Markdown (`.md`) and plain text (`.txt`), if enabled by the loader implementation.
- **PDF extraction:** The `pypdf` package can extract text from text-based PDFs.
- **Limitation:** Scanned PDFs usually need OCR before their text can be ingested. `pypdf` does not perform OCR.

### 2. Text Chunking
- **Role:** Splits extracted document text into smaller pieces so each piece can be embedded and retrieved independently.
- **Strategy:** Character-count chunking.
- **Chunk size:** `600` characters.
- **Overlap:** `100` characters.
- **Purpose of overlap:** Preserves some context across neighboring chunks when a relevant passage crosses a chunk boundary.

Example:
```text
Chunk 1: characters 0–599
Chunk 2: characters 500–1099
Chunk 3: characters 1000–1599



Enterprise_Local_Agentic_RAG/
├── data/
│   └── sample_docs/                 # Documents to ingest
├── scripts/
│   ├── __init__.py
│   ├── ingest.py                    # Runs the ingestion pipeline
│   ├── test_connections.py          # Phase 1 connectivity checks# Phase 2: Document Ingestion & Semantic Retrieval

## 🎯 Goal & Overview
The objective of Phase 2 is to build the document ingestion and retrieval pipeline for the Enterprise Local Agentic RAG project.

The pipeline loads documents, extracts their text, divides the text into overlapping chunks, creates an embedding for each chunk using Ollama, and stores the vectors with their source text and metadata in Qdrant. It also embeds a user query and retrieves the most relevant chunks from the collection.

At the end of this phase, the project can search ingested document content by semantic similarity. The retrieved text can then be supplied to an LLM as context for question answering.

---

## 🏗️ Architecture & Component Roles

### 1. Document Loader
- **Role:** Reads supported files from the project’s document directory and returns their text and source information.
- **Initial input focus:** PDF files.
- **Other formats discussed:** Markdown (`.md`) and plain text (`.txt`), if enabled by the loader implementation.
- **PDF extraction:** The `pypdf` package can extract text from text-based PDFs.
- **Limitation:** Scanned PDFs usually need OCR before their text can be ingested. `pypdf` does not perform OCR.

### 2. Text Chunking
- **Role:** Splits extracted document text into smaller pieces so each piece can be embedded and retrieved independently.
- **Strategy:** Character-count chunking.
- **Chunk size:** `600` characters.
- **Overlap:** `100` characters.
- **Purpose of overlap:** Preserves some context across neighboring chunks when a relevant passage crosses a chunk boundary.

Example:
`Chunk 1: characters 0–599`
`Chunk 2: characters 500–1099`
`Chunk 3: characters 1000–1599`

---

## 📁 Project Structure
```text
Enterprise_Local_Agentic_RAG/
├── data/
│   └── sample_docs/                 # Documents to ingest
├── scripts/
│   ├── __init__.py
│   ├── ingest.py                    # Runs the ingestion pipeline
│   ├── test_connections.py          # Phase 1 connectivity checks
│   └── test_search.py               # Tests semantic retrieval
├── src/
│   ├── config.py
│   ├── core/
│   │   ├── ollama_client.py         # Embeddings and LLM requests
│   │   └── qdrant_client.py         # Collection, upsert, and search
│   └── ingestion/
│       ├── loader.py                # Document loading and text extraction
│       ├── chunker.py               # Character-based text chunking
│       └── pipeline.py              # Coordinates ingestion steps
├── requirements.txt
└── README.md

│   └── test_search.py               # Tests semantic retrieval
├── src/
│   ├── config.py
│   ├── core/
│   │   ├── ollama_client.py         # Embeddings and LLM requests
│   │   └── qdrant_client.py         # Collection, upsert, and search
│   └── ingestion/
│       ├── loader.py                # Document loading and text extraction
│       ├── chunker.py               # Character-based text chunking
│       └── pipeline.py              # Coordinates ingestion steps
├── requirements.txt
└── README.md

![Qdrant Dashboard](https://raw.githubusercontent.com/arash-zare/Enterprise-RAG-Observability/master/readme/images/qdrant_localhost.png)
