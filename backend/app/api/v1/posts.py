from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

# 예시용 Pydantic 모델
class Post(BaseModel):
    id: int
    title: str
    content: str

# 더미 데이터
fake_posts = [
    {"id": 1, "title": "첫 글", "content": "안녕하세요"},
    {"id": 2, "title": "두 번째 글", "content": "반갑습니다"}
]

@router.get("/", response_model=list[Post])
def get_posts():
    return fake_posts


