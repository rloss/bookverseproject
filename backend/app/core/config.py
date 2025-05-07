from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    ENV: str = Field(default="development", description="환경: 개발 or 운영")
    DEBUG: bool = Field(default=True)
    DATABASE_URL: str = "sqlite:///./test.db"

    BACKEND_CORS_ORIGINS: list[str] = ["*"]  # CORS 허용 도메인
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 1일
    SECRET_KEY: str = "your-super-secret-key"

    class Config:
        env_file = ".env"
        extra = "ignore"  # 예기치 않은 .env 값 무시

settings = Settings()
