from qdrant_client import AsyncQdrantClient
from qdrant_client.models import VectorParams, Distance
from src.config import settings

class QdrantManager:
    def __init__(self, host: str = settings.QDRANT_HOST, port: int = settings.QDRANT_PORT):
        self.client = AsyncQdrantClient(host=host, port=port)
        self.collection_name = settings.QDRANT_COLLECTION_NAME

    async def init_collection(self, vector_size: int = settings.EMBEDDING_DIM):
        """ساخت کالکشن در صورت عدم وجود با متریک Cosine"""
        collections = await self.client.get_collections()
        exists = any(c.name == self.collection_name for c in collections.collections)
        
        if not exists:
            await self.client.create_collection(
                collection_name=self.collection_name,
                vectors_config=VectorParams(size=vector_size, distance=Distance.COSINE)
            )
            return f"Collection '{self.collection_name}' created."
        return f"Collection '{self.collection_name}' already exists."

    async def close(self):
        await self.client.close()
