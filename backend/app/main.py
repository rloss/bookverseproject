from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1 import posts

app = FastAPI()

# CORS 설정 (개발용으로 모든 도메인 허용)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 배포시엔 실제 도메인으로 변경!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 라우터 등록
app.include_router(posts.router, prefix="/api/v1/posts", tags=["posts"])
print("📦 등록된 라우트 목록:")
for route in app.router.routes:
    print(f"  - {route.path} ({route.methods})")

@app.get("/")
def root():
    return {"message": "📚 Bookverse API is running"}