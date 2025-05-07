import os

# 디렉토리 및 파일 생성 함수

def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        elif isinstance(content, str):
            os.makedirs(base_path, exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)

# 전체 프로젝트 디렉토리 구조 정의
project_structure = {
    "frontend": {
        ".env.production": "NEXT_PUBLIC_API_URL=https://bookverse-backend.onrender.com\nNODE_VERSION=18.17.1\nPORT=3000",
        "app": {
            "layout.tsx": "export default function Layout({ children }: { children: React.ReactNode }) {\n  return <>{children}</>;\n}",
            "page.tsx": "export default function Home() {\n  return <main>홈입니다</main>;\n}"
        },
        "components": {
            "layout": {},
            "ui": {},
            "post": {},
            "animations": {}
        },
        "lib": {
            "api.ts": "// API 함수",
            "auth.ts": "// 인증 유틸",
            "utils.ts": "// 공통 유틸"
        },
        "public": {},
        "styles": {
            "globals.css": "/* Tailwind base 설정 */\n@tailwind base;\n@tailwind components;\n@tailwind utilities;"
        },
        "tailwind.config.ts": "module.exports = { darkMode: 'class', content: ['./app/**/*.{ts,tsx}'], theme: { extend: {} }, plugins: [] };",
        "tsconfig.json": "{\n  \"compilerOptions\": {\n    \"target\": \"esnext\",\n    \"module\": \"esnext\",\n    \"jsx\": \"preserve\",\n    \"strict\": true\n  }\n}"
    },
    "backend": {
        "app": {
            "main.py": "from fastapi import FastAPI\nfrom app.api.v1 import users, posts\nfrom fastapi.middleware.cors import CORSMiddleware\n\napp = FastAPI()\n\n# CORS\napp.add_middleware(\n    CORSMiddleware,\n    allow_origins=[\"*\"],\n    allow_credentials=True,\n    allow_methods=[\"*\"],\n    allow_headers=[\"*\"],\n)\n\n# Routers\napp.include_router(users.router, prefix='/api/v1/users')\napp.include_router(posts.router, prefix='/api/v1/posts')",
            "api": {
                "v1": {
                    "users.py": "from fastapi import APIRouter\nrouter = APIRouter()\n@router.get('/')\ndef get_users(): return ['user1', 'user2']",
                    "auth.py": "",
                    "posts.py": "from fastapi import APIRouter\nrouter = APIRouter()\n@router.get('/')\ndef get_posts(): return ['post1', 'post2']",
                    "groups.py": "",
                    "books.py": "",
                    "schedules.py": "",
                    "comments.py": ""
                },
                "deps.py": ""
            },
            "models": {
                "user.py": "",
                "post.py": "",
                "group.py": "",
                "book.py": "",
                "comment.py": ""
            },
            "schemas": {
                "user.py": "",
                "post.py": "",
                "auth.py": "",
                "group.py": "",
                "schedule.py": ""
            },
            "services": {
                "user_service.py": "",
                "post_service.py": "",
                "group_service.py": "",
                "auth_service.py": "",
                "utils.py": ""
            },
            "db": {
                "base.py": "",
                "session.py": "",
                "init_db.py": ""
            },
            "core": {
                "config.py": "",
                "security.py": "",
                "exceptions.py": "",
                "logging.py": ""
            },
            "utils": {
                "id_generator.py": "",
                "datetime.py": "",
                "hashing.py": ""
            }
        },
        "tests": {
            "test_users.py": "",
            "test_posts.py": "",
            "conftest.py": ""
        },
        "alembic": {
            "versions": {},
            "env.py": ""
        },
        "requirements.txt": "fastapi\nsqlalchemy\npydantic\nudicorn[standard]",
        ".env": "DATABASE_URL=postgresql://user:pass@localhost:5432/app"
    },
    ".env.example": "DATABASE_URL=postgresql://user:pass@localhost:5432/app",
    ".gitignore": "__pycache__\nnode_modules\n.env\n.next\n*.pyc",
    "README.md": "# Bookverse Fullstack Monorepo\n\n## 📦 구조\n- frontend/: Next.js + Tailwind + API 연동\n- backend/: FastAPI + PostgreSQL + REST API\n\n## 🧪 배포 (Render 기준)\n- frontend → Web Service: root directory 'frontend' 지정\n- backend → Web Service: root directory 'backend' 지정",
    "docker-compose.yml": "version: '3.8'\nservices:\n  backend:\n    build: ./backend\n    ports:\n      - '8000:8000'\n  frontend:\n    build: ./frontend\n    ports:\n      - '3000:3000'"
}

# 실행
if __name__ == "__main__":
    create_structure("./", project_structure)
    print("✅ 디렉토리 및 초기 파일 생성 완료!")
