from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    GEMINI_API_KEY: str = Field(default="")
    GOOGLE_API_KEY: str = Field(default="")  # fallback
    APP_ENV: str = Field(default="development")
    APP_PORT: int = Field(default=8000)

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
