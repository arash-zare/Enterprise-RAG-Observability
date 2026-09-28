import asyncio
from src.core.ollama_client import OllamaClient
from src.core.qdrant_client import QdrantManager


async def ask(query: str):
    ollama = OllamaClient()
    qdrant = QdrantManager()

    try:
        print(f"❓ سوال شما: {query}\n")

        # ۱. تبدیل سوال به بردار
        query_vector = await ollama.get_embedding(query)

        # ۲. سرچ مرتبط‌ترین چانک‌ها از Qdrant
        hits = await qdrant.search(query_vector=query_vector, limit=2)

        if not hits:
            print("❌ هیچ محتوای مرتبطی در Qdrant پیدا نشد!")
            return

        # ۳. ساخت Context از نتایج بازگشتی
        context = "\n---\n".join([hit.payload.get("text", "") for hit in hits])

        # ۴. ساخت پرامپت RAG
        prompt = f"""You are a helpful assistant. Use ONLY the following context to answer the question.
If the answer is not contained in the context, say "I don't know based on the provided document."

Context:
{context}

Question: {query}
Answer:"""

        print("🤖 در حال تولید پاسخ توسط Qwen بر اساس محتوای سند...\n")

        # ۵. فراخوانی متد درست: generate_response
        response = await ollama.generate_response(prompt)
        print("💡 پاسخ:")
        print(response)

    finally:
        await qdrant.close()


if __name__ == "__main__":
    # سوال تستی مرتبط با متنی که ingest کردی
    user_query = "arash has website?"
    asyncio.run(ask(user_query))
