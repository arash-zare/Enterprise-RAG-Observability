import asyncio
from src.core.ollama_client import OllamaClient
from src.core.qdrant_client import QdrantManager


async def main():
    ollama = OllamaClient()
    qdrant = QdrantManager()

    # سوال یا موضوعی که می‌خواهیم معنایی جستجو کنیم
    query = "How are alerts handled and visualized in monitoring?"
    print(f"🔎 Query: '{query}'\n")

    # ۱. تبدیل سوال کاربر به بردار عددی ۷۶۸ بعدی
    query_vector = await ollama.get_embedding(query)

    # ۲. جستجوی نزدیک‌ترین چانک‌ها در Qdrant (Cosine Similarity)
    search_results = await qdrant.search(query_vector=query_vector, limit=2)

    print("--- 🎯 Top Search Results from Qdrant ---")
    for idx, hit in enumerate(search_results, start=1):
        score = hit.score
        source = hit.payload.get("source")
        text = hit.payload.get("text")
        print(f"\n[{idx}] Score (Similarity): {score:.4f} | Source: {source}")
        print(f"Content:\n{text}")

    await qdrant.close()


if __name__ == "__main__":
    asyncio.run(main())
