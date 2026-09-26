# Enterprise Local Agentic RAG & Observability Engine

[![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-009688.svg?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Qdrant](https://img.shields.io/badge/Vector_DB-Qdrant-red.svg?logo=qdrant)](https://qdrant.tech/)
[![Ollama](https://img.shields.io/badge/LLM_Engine-Ollama-black.svg?logo=ollama)](https://ollama.com)
[![Prometheus](https://img.shields.io/badge/Monitoring-Prometheus-E6522C.svg?logo=prometheus&logoColor=white)](https://prometheus.io/)
[![Grafana](https://img.shields.io/badge/Dashboard-Grafana-F46800.svg?logo=grafana&logoColor=white)](https://grafana.com/)
[![Docker](https://img.shields.io/badge/Deployment-Docker_Compose-2496ED.svg?logo=docker&logoColor=white)](https://www.docker.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **Status:** 🚧 Active Development (Phased Implementation)

A production-ready, privacy-first, and fully self-hosted **Retrieval-Augmented Generation (RAG)** service powered by local LLMs, lightweight vector search, agentic routing, and end-to-end LLM observability.

---

## 🎯 Overview & Problem Statement

Most enterprise knowledge retrieval prototypes rely on external LLM APIs (e.g., OpenAI, Anthropic), introducing high recurring costs, network latency, and critical data privacy risks. Moreover, many implementations lack essential software engineering rigor: observability, structured error handling, and containerized deployment.

**This project delivers:**
1. **100% On-Premise & Air-Gapped Readiness:** Runs entirely on commodity hardware without sending proprietary data to third-party endpoints.
2. **Agentic Knowledge Routing:** Distinguishes between direct Q&A, context-heavy document retrieval, and structured fallback.
3. **First-Class Observability (LLMOps):** Tracks token consumption, retrieval latency, request volume, and cache hit ratios via Prometheus and Grafana.
4. **Clean Engineering Standards:** Built with FastAPI (async), Pydantic V2 validation, Qdrant vector database, and modular Docker orchestration.

---

## 🏗 System Architecture
```mermaid
flowchart TD
Client([Client / Application]) -->|HTTP REST / SSE| API[FastAPI Gateway]

subgraph Core Engine
API --> Router{Agentic Router}
Router -->|Direct Prompt / Tool Call| LLM[Local LLM - Ollama]
Router -->|Context Retrieval Needed| Retriever[Qdrant Vector DB]
Retriever -->|Relevant Chunks + Metadata| ReRanker[Context Assembler]
ReRanker --> LLM
end

subgraph Observability Stack
API -.->|Request / Latency Metrics| Prom[Prometheus Server]
LLM -.->|TTFT & Token Usage| Prom
Prom --> Grafana[Grafana Dashboards]
end

subgraph Data Ingestion Pipeline
Docs[Raw Documents / PDFs] --> Chunker[Semantic / Recursive Splitter]
Chunker --> Embedder[Local Embedding Model]
Embedder -->|Dense Vectors| Retriever
end

---

## ⚙️ Tech Stack

| Component | Technology | Rationale |
| :--- | :--- | :--- |
| **Backend / API** | Python 3.11+, FastAPI | High-throughput asynchronous REST API with native OpenAPI documentation |
| **LLM Inference** | Ollama (`Hermes-3` / `Qwen2.5`) | Optimized local quantized inference with strong function-calling support |
| **Vector Store** | Qdrant | Ultra-fast Rust-based vector search with native metadata filtering and low footprint |
| **Embeddings** | `bge-small-en-v1.5` / `nomic-embed` | State-of-the-art embedding quality under 500MB memory usage |
| **Observability** | Prometheus + Grafana | Production-grade metric aggregation (latency, throughput, token rates) |
| **Orchestration** | Docker & Docker Compose | Single-command reproducible environment with isolated health checks |

---

## 🚀 Key Use Cases

- **Internal Knowledge Base:** Instant semantic search and Q&A over internal technical docs, runbooks, and policies.
- **Support / DevOps Troubleshooting:** Querying architecture documentation and post-mortem logs locally without third-party API exposure.
- **Cost-Controlled Retrieval:** Zero variable API billing for search and summarization workloads.

---

## 🗺 Implementation Roadmap

- [ ] **Phase 1: Infrastructure & Model Runtime**
  - [x] Repository setup and architecture baseline
  - [ ] Docker Compose setup for Ollama, Qdrant, and network bridging
  - [ ] Healthcheck automation and local model pulling scripts
- [ ] **Phase 2: Ingestion & Vector Pipeline**
  - [ ] Document loaders (Markdown, PDF, TXT)
  - [ ] Chunking strategy with metadata preservation
  - [ ] Embedding pipeline and upserting into Qdrant collections
- [ ] **Phase 3: Core API & Agentic Routing**
  - [ ] FastAPI asynchronous service structure with Pydantic V2
  - [ ] Routing logic: Direct response vs. Knowledge retrieval
  - [ ] Context assembly and structured generation
- [ ] **Phase 4: LLMOps & Observability**
  - [ ] Custom Prometheus middleware for API metrics
  - [ ] Latency tracking (Time-To-First-Token, retrieval latency)
  - [ ] Provisioned Grafana dashboard configuration
- [ ] **Phase 5: Evaluation & Production Hardening**
  - [ ] Retrieval evaluation tests (Context relevance & hit rate)
  - [ ] End-to-end integration tests
  - [ ] Production deployment guidelines

---

## 🛠 Quickstart (Coming in Phase 1)

bash
# Clone the repository
git clone https://github.com/arash-zare/Enterprise-RAG-Observability.git
cd enterprise-local-rag

# Spin up infrastructure
docker compose up -d

# Check service readiness
curl http://localhost:8000/health

---

## 👤 Author

Developed by **Arash Zare**  
- LinkedIn: [arash-zare-dev](https://www.linkedin.com/in/arash-zare-dev)  
- Website: [arashzare.ir](https://arashzare.ir)  
- GitHub: [@arash-zare](https://github.com/arash-zare)


---
