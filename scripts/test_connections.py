import asyncio
from src.core.ollama_client import OllamaClient
from src.core.qdrant_client import QdrantManager
from src.config import settings

async def main():
    print("🔍 Testing connections and setup...")
    
    # 1. Test Ollama Embedding
    ollama = OllamaClient()
    try:
        sample_vec = await ollama.get_embedding("Enterprise Observability RAG")
        print(f"✅ Ollama Embedding OK (Dimensions: {len(sample_vec)})")
    except Exception as e:
        print(f"❌ Ollama Embedding Failed: {e}")

    # 2. Test Ollama LLM
    try:
        reply = await ollama.generate_response("Say 'RAG Stack Ready' in 3 words.")
        print(f"✅ Ollama LLM OK (Response: {reply.strip()})")
    except Exception as e:
        print(f"❌ Ollama LLM Failed: {e}")

    # 3. Test Qdrant Collection Initialization
    qdrant = QdrantManager()
    try:
        res = await qdrant.init_collection(vector_size=settings.EMBEDDING_DIM)
        print(f"✅ Qdrant OK ({res})")
    except Exception as e:
        print(f"❌ Qdrant Failed: {e}")
    finally:
        await qdrant.close()

if __name__ == "__main__":
    asyncio.run(main())
