import uuid
from src.config import settings
from src.core.ollama_client import OllamaClient
from src.core.qdrant_client import QdrantManager
from src.ingestion.loader import load_documents
from src.ingestion.chunker import chunk_text


async def ingest_pipeline(
    data_dir: str = "data/sample_docs",
    chunk_size: int = 600,
    overlap: int = 100,
) -> dict:
    # ۱. بارگذاری فایل‌ها (PDF / TXT / MD)
    docs = load_documents(data_dir)
    if not docs:
        print("⚠️ No documents found to ingest.")
        return {"status": "empty", "upserted": 0}

    ollama = OllamaClient()
    qdrant = QdrantManager()

    # ۲. اطمینان از وجود کالکشن
    await qdrant.init_collection(vector_size=settings.EMBEDDING_DIM)

    total_chunks = 0
    all_points = []

    print("⚙️ Processing documents and generating embeddings...")

    # ۳. چانکینگ و تبدیل به بردار
    for doc in docs:
        chunks = chunk_text(
            source=doc.source,
            text=doc.text,
            chunk_size=chunk_size,
            overlap=overlap,
        )
        total_chunks += len(chunks)

        for chunk in chunks:
            # دریافت بردار امبدینگ از Ollama
            vector = await ollama.get_embedding(chunk.text)

            all_points.append(
                {
                    "id": str(uuid.uuid4()),
                    "vector": vector,
                    "payload": {
                        "source": chunk.source,
                        "chunk_id": chunk.chunk_id,
                        "text": chunk.text,
                    },
                }
            )

    # ۴. ذخیره در Qdrant
    if all_points:
        await qdrant.upsert(all_points)
        print(f"🚀 Successfully stored {len(all_points)} vectors in Qdrant.")

    # await ollama.close()
    await qdrant.close()

    return {
        "status": "success",
        "documents_count": len(docs),
        "chunks_count": total_chunks,
        "upserted_points": len(all_points),
    }




