# Phase 1: Local Infrastructure Setup & Service Health Verification

## 🎯 Goal & Overview
The primary objective of Phase 1 is to establish a secure, local, and reproducible containerized infrastructure for our Enterprise Agentic RAG pipeline. This phase ensures that the LLM/Embedding runtime (**Ollama**) and the Vector Database (**Qdrant**) are fully operational, exposed via predictable networks/ports, and verified through automated asynchronous Python health checks.

---

## 🏗️ Architecture & Component Roles



### 1. Ollama (Inference Engine)
- **Role:** Self-hosted runtime serving local models without external API calls or data leakage.
- **Models Pulled:**
  - `nomic-embed-text:latest`: Text embedding model mapping inputs to **768-dimensional** dense vectors.
  - `qwen2.5:3b`: Lightweight, instruction-tuned LLM (Context window: 32,768 tokens) used for synthesis and agentic routing.
- **Port:** `11434` (HTTP REST).

### 2. Qdrant (Vector Database)
- **Role:** High-performance, memory-efficient vector store designed for semantic vector indexing, payload storage, and similarity searches.
- **Distance Metric:** **Cosine Similarity** ($\text{Cosine Distance} = 1 - \cos(\theta)$), optimal for normalized direction-based semantic matching.
- **Vector Dimension:** **768** (strictly matching the embedding dimension of `nomic-embed-text`).
- **Ports:** `6333` (REST HTTP API & Web Dashboard), `6334` (Internal gRPC communication).

### 3. Orchestration & App Layer (Python 3.11+)
- **`src/config.py`**: Type-safe environment management powered by `pydantic-settings`.
- **`src/core/ollama_client.py`**: Asynchronous HTTP client wrapping Ollama's `/api/embeddings` and `/api/generate`.
- **`src/core/qdrant_client.py`**: Wrapper around `AsyncQdrantClient` for automated collection lifecycle management (`init_collection`).

---

## 📂 Project Structure (Phase 1 State)
```text
Enterprise_Local_Agentic_RAG/
├── docker/
│   └── docker-compose.yml       # Service definitions for Ollama & Qdrant
├── scripts/
│   ├── __init__.py
│   └── test_connections.py     # End-to-end integration & smoke test
├── src/
│   ├── __init__.py
│   ├── config.py               # Pydantic BaseSettings loading .env
│   └── core/
│       ├── __init__.py
│       ├── ollama_client.py    # Async Ollama HTTP wrapper
│       └── qdrant_client.py    # Async Qdrant client & collection initializer
├── .env                         # Local environment variables
├── requirements.txt             # Project dependencies
└── README.md
