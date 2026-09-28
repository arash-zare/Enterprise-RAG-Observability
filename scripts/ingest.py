import asyncio
from src.ingestion.pipeline import ingest_pipeline

if __name__ == "__main__":
    result = asyncio.run(ingest_pipeline())
    print("Result:", result)
