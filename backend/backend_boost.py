import os

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

# 템플릿
router_template = """from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_items():
    return ["sample"]
"""

model_template = """from sqlalchemy import Column, Integer, String
from app.db.base import Base

class Sample(Base):
    __tablename__ = "samples"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
"""

schema_template = """from pydantic import BaseModel

class SampleCreate(BaseModel):
    title: str

class SampleOut(SampleCreate):
    id: int
"""

service_template = """from app.models.sample import Sample

def get_mock_samples():
    return ["sample1", "sample2"]
"""

base_template = """from sqlalchemy.orm import declarative_base
Base = declarative_base()
"""

session_template = """from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
"""

config_template = """from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./test.db"

    class Config:
        env_file = ".env"

settings = Settings()
"""

deps_template = """# Depends 예시
def get_current_user():
    return {"id": "mock-user-id"}
"""

def build_backend_boost():
    modules = ["users", "auth", "posts", "groups", "books", "schedules", "comments"]
    for name in modules:
        write_file(f"backend/app/api/v1/{name}.py", router_template)

    write_file("backend/app/api/deps.py", deps_template)
    write_file("backend/app/models/post.py", model_template)
    write_file("backend/app/schemas/post.py", schema_template)
    write_file("backend/app/services/post_service.py", service_template)
    write_file("backend/app/db/base.py", base_template)
    write_file("backend/app/db/session.py", session_template)
    write_file("backend/app/core/config.py", config_template)

if __name__ == "__main__":
    build_backend_boost()
    print("✅ backend 템플릿 생성 완료!")
