import httpx
from src.config import settings

class OllamaClient:
    def __init__(self, base_url: str = settings.OLLAMA_BASE_URL):
        self.base_url = base_url.rstrip("/")

    async def get_embedding(self, text: str, model: str = settings.EMBEDDING_MODEL) -> list[float]:
        """تولید وکتور امبدینگ از طریق اندپوینت Ollama"""
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.post(
                f"{self.base_url}/api/embeddings",
                json={"model": model, "prompt": text}
            )
            response.raise_for_status()
            data = response.json()
            return data["embedding"]

    async def generate_response(self, prompt: str, system_prompt: str = "", model: str = settings.LLM_MODEL) -> str:
        """تولید پاسخ متنی از LLM"""
        async with httpx.AsyncClient(timeout=60.0) as client:
            payload = {
                "model": model,
                "prompt": prompt,
                "stream": False
            }
            if system_prompt:
                payload["system"] = system_prompt

            response = await client.post(f"{self.base_url}/api/generate", json=payload)
            response.raise_for_status()
            return response.json().get("response", "")
