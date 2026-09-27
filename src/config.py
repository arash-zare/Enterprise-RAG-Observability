from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Ports & URLs
    OLLAMA_BASE_URL: str = "http://localhost:11434"
    QDRANT_HOST: str = "localhost"
    QDRANT_PORT: int = 6333
    QDRANT_COLLECTION_NAME: str = "enterprise_knowledge_base"

    # Models
    LLM_MODEL: str = "qwen2.5:3b"
    EMBEDDING_MODEL: str = "nomic-embed-text:latest"
    EMBEDDING_DIM: int = 768

    # App
    API_PORT: int = 8000
    LOG_LEVEL: str = "INFO"
    APP_ENV: str = "development"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

settings = Settings()
