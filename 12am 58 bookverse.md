# 📁 프로젝트 구조

```
├── 📄 .env.example
├── 📄 .gitignore
├── 📄 README.md
├── 📁 backend
│   ├── 📄 .env
│   ├── 📁 alembic
│   │   ├── 📄 env.py
│   │   └── 📁 versions
│   ├── 📁 app
│   │   ├── 📁 api
│   │   │   ├── 📄 deps.py
│   │   │   └── 📁 v1
│   │   │       ├── 📄 auth.py
│   │   │       ├── 📄 books.py
│   │   │       ├── 📄 comments.py
│   │   │       ├── 📄 groups.py
│   │   │       ├── 📄 posts.py
│   │   │       ├── 📄 schedules.py
│   │   │       └── 📄 users.py
│   │   ├── 📁 core
│   │   │   ├── 📄 config.py
│   │   │   ├── 📄 exceptions.py
│   │   │   ├── 📄 logging.py
│   │   │   └── 📄 security.py
│   │   ├── 📁 db
│   │   │   ├── 📄 base.py
│   │   │   ├── 📄 init_db.py
│   │   │   └── 📄 session.py
│   │   ├── 📄 main.py
│   │   ├── 📁 models
│   │   │   ├── 📄 book.py
│   │   │   ├── 📄 comment.py
│   │   │   ├── 📄 group.py
│   │   │   ├── 📄 post.py
│   │   │   └── 📄 user.py
│   │   ├── 📁 schemas
│   │   │   ├── 📄 auth.py
│   │   │   ├── 📄 group.py
│   │   │   ├── 📄 post.py
│   │   │   ├── 📄 schedule.py
│   │   │   └── 📄 user.py
│   │   ├── 📁 services
│   │   │   ├── 📄 auth_service.py
│   │   │   ├── 📄 group_service.py
│   │   │   ├── 📄 post_service.py
│   │   │   ├── 📄 user_service.py
│   │   │   └── 📄 utils.py
│   │   └── 📁 utils
│   │       ├── 📄 datetime.py
│   │       ├── 📄 hashing.py
│   │       └── 📄 id_generator.py
│   ├── 📄 render.yaml
│   ├── 📄 requirements.txt
│   └── 📁 tests
│       ├── 📄 conftest.py
│       ├── 📄 test_posts.py
│       └── 📄 test_users.py
├── 📄 docker-compose.yml
├── 📁 frontend
│   ├── 📄 .env.production
│   ├── 📁 app
│   │   ├── 📁 books
│   │   │   └── 📄 page.tsx
│   │   ├── 📁 groups
│   │   │   └── 📁 [groupId]
│   │   │       ├── 📁 me
│   │   │       │   └── 📄 page.tsx
│   │   │       ├── 📄 page.tsx
│   │   │       ├── 📁 posts
│   │   │       │   └── 📁 [postId]
│   │   │       │       └── 📄 page.tsx
│   │   │       └── 📁 write
│   │   │           └── 📄 page.tsx
│   │   ├── 📄 layout.tsx
│   │   ├── 📁 login
│   │   │   └── 📄 page.tsx
│   │   ├── 📁 my
│   │   │   └── 📄 page.tsx
│   │   ├── 📄 page.tsx
│   │   ├── 📁 posts
│   │   │   └── 📁 [postId]
│   │   │       └── 📄 page.tsx
│   │   ├── 📁 signup
│   │   │   └── 📄 page.tsx
│   │   └── 📁 write
│   │       └── 📄 page.tsx
│   ├── 📁 components
│   │   ├── 📁 animations
│   │   ├── 📁 layout
│   │   ├── 📁 post
│   │   └── 📁 ui
│   ├── 📁 lib
│   │   ├── 📄 api.ts
│   │   ├── 📄 auth.ts
│   │   └── 📄 utils.ts
│   ├── 📄 next-env.d.ts
│   ├── 📄 package-lock.json
│   ├── 📄 package.json
│   ├── 📄 postcss.config.js
│   ├── 📁 public
│   ├── 📄 setup.py
│   ├── 📁 styles
│   │   └── 📄 globals.css
│   ├── 📄 tailwind.config.ts
│   └── 📄 tsconfig.json
├── 📄 setsetup.py
├── 📄 setup.py
```

## 📄 `.env.example`

```
DATABASE_URL=postgresql://user:pass@localhost:5432/app
```

## 📄 `.gitignore`

```
__pycache__
node_modules
.env
.next
*.pyc
```

## 📄 `docker-compose.yml`

```yaml
version: '3.8'
services:
  backend:
    build: ./backend
    ports:
      - '8000:8000'
  frontend:
    build: ./frontend
    ports:
      - '3000:3000'
```

## 📄 `README.md`

```markdown
# Bookverse Fullstack Monorepo

## 📦 구조
- frontend/: Next.js + Tailwind + API 연동
- backend/: FastAPI + PostgreSQL + REST API

## 🧪 배포 (Render 기준)
- frontend → Web Service: root directory 'frontend' 지정
- backend → Web Service: root directory 'backend' 지정
```

## 📄 `setsetup.py`

```python
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
            "layout.tsx": "export default function Layout({ children }: { children: React.ReactNode }) {\n  return (\n    <html lang=\"en\">\n      <body>\n        <header style={{ padding: '1rem', backgroundColor: '#f5f5f5', fontWeight: 'bold' }}>\n          Bookverse\n        </header>\n        <main style={{ padding: '1rem' }}>{children}</main>\n      </body>\n    </html>\n  );\n}",
            "page.tsx": "export default function Home() {\n  return (\n    <div style={{ textAlign: 'center', marginTop: '10%' }}>\n      <h1 style={{ fontSize: '2rem', fontWeight: 'bold' }}>Welcome to Bookverse 📚</h1>\n      <p style={{ marginTop: '1rem' }}>당신의 독서 모임, 지금 시작하세요.</p>\n    </div>\n  );\n}"
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

```

## 📄 `setup.py`

```python
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
        "app": {
            "layout.tsx": "// layout",
            "page.tsx": "// 홈 페이지",
            "groups": {
                "[groupId]": {
                    "page.tsx": "// 그룹 대시보드",
                    "posts": {
                        "[postId]": {
                            "page.tsx": "// 글 상세"
                        }
                    },
                    "write": {
                        "page.tsx": "// 그룹 글쓰기"
                    },
                    "me": {
                        "page.tsx": "// 그룹 내 마이페이지"
                    }
                }
            },
            "my": {
                "page.tsx": "// 전역 마이페이지"
            },
            "posts": {
                "[postId]": {
                    "page.tsx": "// 개인 글 상세"
                }
            },
            "write": {
                "page.tsx": "// 개인 글쓰기"
            },
            "login": {"page.tsx": "// 로그인"},
            "signup": {"page.tsx": "// 회원가입"},
            "books": {"page.tsx": "// 도서 탐색"}
        },
        "components": {
            "layout": {},
            "ui": {},
            "post": {},
            "animations": {}
        },
        "lib": {
            "api.ts": "// API 함수들",
            "auth.ts": "// 인증 상태 관리",
            "utils.ts": "// 유틸 함수"
        },
        "public": {},
        "styles": {
            "globals.css": "/* 글로벌 스타일 */"
        },
        "tailwind.config.ts": "",
        "tsconfig.json": "",
        "package.json": ""
    },
    "backend": {
        "app": {
            "main.py": "# FastAPI 진입점",
            "api": {
                "v1": {
                    "users.py": "",
                    "auth.py": "",
                    "posts.py": "",
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
        "requirements.txt": "",
        ".env": ""
    },
    ".env.example": "",
    ".gitignore": "",
    "README.md": "",
    "docker-compose.yml": ""
}

# 실행
if __name__ == "__main__":
    create_structure("./", project_structure)
    print("✅ 디렉토리 구조 생성 완료!")

```

## 📄 `좀_백업.md`

```markdown
# 📁 프로젝트 구조

```
├── 📄 .env.example
├── 📄 .gitignore
├── 📄 README.md
├── 📁 backend
│   ├── 📄 .env
│   ├── 📁 alembic
│   │   ├── 📄 env.py
│   │   └── 📁 versions
│   ├── 📁 app
│   │   ├── 📁 api
│   │   │   ├── 📄 deps.py
│   │   │   └── 📁 v1
│   │   │       ├── 📄 auth.py
│   │   │       ├── 📄 books.py
│   │   │       ├── 📄 comments.py
│   │   │       ├── 📄 groups.py
│   │   │       ├── 📄 posts.py
│   │   │       ├── 📄 schedules.py
│   │   │       └── 📄 users.py
│   │   ├── 📁 core
│   │   │   ├── 📄 config.py
│   │   │   ├── 📄 exceptions.py
│   │   │   ├── 📄 logging.py
│   │   │   └── 📄 security.py
│   │   ├── 📁 db
│   │   │   ├── 📄 base.py
│   │   │   ├── 📄 init_db.py
│   │   │   └── 📄 session.py
│   │   ├── 📄 main.py
│   │   ├── 📁 models
│   │   │   ├── 📄 book.py
│   │   │   ├── 📄 comment.py
│   │   │   ├── 📄 group.py
│   │   │   ├── 📄 post.py
│   │   │   └── 📄 user.py
│   │   ├── 📁 schemas
│   │   │   ├── 📄 auth.py
│   │   │   ├── 📄 group.py
│   │   │   ├── 📄 post.py
│   │   │   ├── 📄 schedule.py
│   │   │   └── 📄 user.py
│   │   ├── 📁 services
│   │   │   ├── 📄 auth_service.py
│   │   │   ├── 📄 group_service.py
│   │   │   ├── 📄 post_service.py
│   │   │   ├── 📄 user_service.py
│   │   │   └── 📄 utils.py
│   │   └── 📁 utils
│   │       ├── 📄 datetime.py
│   │       ├── 📄 hashing.py
│   │       └── 📄 id_generator.py
│   ├── 📄 render.yaml
│   ├── 📄 requirements.txt
│   └── 📁 tests
│       ├── 📄 conftest.py
│       ├── 📄 test_posts.py
│       └── 📄 test_users.py
├── 📄 docker-compose.yml
├── 📁 frontend
│   ├── 📄 .env.production
│   ├── 📁 app
│   │   ├── 📁 books
│   │   │   └── 📄 page.tsx
│   │   ├── 📁 groups
│   │   │   └── 📁 [groupId]
│   │   │       ├── 📁 me
│   │   │       │   └── 📄 page.tsx
│   │   │       ├── 📄 page.tsx
│   │   │       ├── 📁 posts
│   │   │       │   └── 📁 [postId]
│   │   │       │       └── 📄 page.tsx
│   │   │       └── 📁 write
│   │   │           └── 📄 page.tsx
│   │   ├── 📄 layout.tsx
│   │   ├── 📁 login
│   │   │   └── 📄 page.tsx
│   │   ├── 📁 my
│   │   │   └── 📄 page.tsx
│   │   ├── 📄 page.tsx
│   │   ├── 📁 posts
│   │   │   └── 📁 [postId]
│   │   │       └── 📄 page.tsx
│   │   ├── 📁 signup
│   │   │   └── 📄 page.tsx
│   │   └── 📁 write
│   │       └── 📄 page.tsx
│   ├── 📁 components
│   │   ├── 📁 animations
│   │   ├── 📁 layout
│   │   ├── 📁 post
│   │   └── 📁 ui
│   ├── 📁 lib
│   │   ├── 📄 api.ts
│   │   ├── 📄 auth.ts
│   │   └── 📄 utils.ts
│   ├── 📄 next-env.d.ts
│   ├── 📄 package-lock.json
│   ├── 📄 package.json
│   ├── 📄 postcss.config.js
│   ├── 📁 public
│   ├── 📄 setup.py
│   ├── 📁 styles
│   │   └── 📄 globals.css
│   ├── 📄 tailwind.config.ts
│   └── 📄 tsconfig.json
├── 📄 setsetup.py
├── 📄 setup.py
└── 📄 좀_백업.md
```

## 📄 `.env.example`

```
DATABASE_URL=postgresql://user:pass@localhost:5432/app
```

## 📄 `.gitignore`

```
__pycache__
node_modules
.env
.next
*.pyc
```

## 📄 `docker-compose.yml`

```yaml
version: '3.8'
services:
  backend:
    build: ./backend
    ports:
      - '8000:8000'
  frontend:
    build: ./frontend
    ports:
      - '3000:3000'
```

## 📄 `README.md`

```markdown
# Bookverse Fullstack Monorepo

## 📦 구조
- frontend/: Next.js + Tailwind + API 연동
- backend/: FastAPI + PostgreSQL + REST API

## 🧪 배포 (Render 기준)
- frontend → Web Service: root directory 'frontend' 지정
- backend → Web Service: root directory 'backend' 지정
```

## 📄 `setsetup.py`

```python
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
            "layout.tsx": "export default function Layout({ children }: { children: React.ReactNode }) {\n  return (\n    <html lang=\"en\">\n      <body>\n        <header style={{ padding: '1rem', backgroundColor: '#f5f5f5', fontWeight: 'bold' }}>\n          Bookverse\n        </header>\n        <main style={{ padding: '1rem' }}>{children}</main>\n      </body>\n    </html>\n  );\n}",
            "page.tsx": "export default function Home() {\n  return (\n    <div style={{ textAlign: 'center', marginTop: '10%' }}>\n      <h1 style={{ fontSize: '2rem', fontWeight: 'bold' }}>Welcome to Bookverse 📚</h1>\n      <p style={{ marginTop: '1rem' }}>당신의 독서 모임, 지금 시작하세요.</p>\n    </div>\n  );\n}"
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

```

## 📄 `backend\.env`

```
DATABASE_URL=postgresql://user:pass@localhost:5432/app
```

## 📄 `backend\render.yaml`

```yaml
services:
  - type: web
    name: bookclub-backend
    env: python
    buildCommand: "pip install -r requirements.txt"
    startCommand: "uvicorn app.main:app --host 0.0.0.0 --port 8000"
    plan: free
    region: oregon
    envVars:
      - key: DATABASE_URL
        sync: false  # Render 환경변수 UI에서 수동 입력

```

## 📄 `backend\requirements.txt`

```
fastapi
sqlalchemy
pydantic
uvicorn[standard]
```

## 📄 `backend\alembic\env.py`

```python

```

## 📄 `backend\app\main.py`

```python
from fastapi import FastAPI
from app.api.v1 import users, posts
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(users.router, prefix='/api/v1/users')
app.include_router(posts.router, prefix='/api/v1/posts')
```

## 📄 `backend\app\api\deps.py`

```python

```

## 📄 `backend\app\api\v1\auth.py`

```python

```

## 📄 `backend\app\api\v1\books.py`

```python

```

## 📄 `backend\app\api\v1\comments.py`

```python

```

## 📄 `backend\app\api\v1\groups.py`

```python

```

## 📄 `backend\app\api\v1\posts.py`

```python
from fastapi import APIRouter
router = APIRouter()
@router.get('/')
def get_posts(): return ['post1', 'post2']
```

## 📄 `backend\app\api\v1\schedules.py`

```python

```

## 📄 `backend\app\api\v1\users.py`

```python
from fastapi import APIRouter
router = APIRouter()
@router.get('/')
def get_users(): return ['user1', 'user2']
```

## 📄 `backend\app\core\config.py`

```python

```

## 📄 `backend\app\core\exceptions.py`

```python

```

## 📄 `backend\app\core\logging.py`

```python

```

## 📄 `backend\app\core\security.py`

```python

```

## 📄 `backend\app\db\base.py`

```python

```

## 📄 `backend\app\db\init_db.py`

```python

```

## 📄 `backend\app\db\session.py`

```python

```

## 📄 `backend\app\models\book.py`

```python

```

## 📄 `backend\app\models\comment.py`

```python

```

## 📄 `backend\app\models\group.py`

```python

```

## 📄 `backend\app\models\post.py`

```python

```

## 📄 `backend\app\models\user.py`

```python

```

## 📄 `backend\app\schemas\auth.py`

```python

```

## 📄 `backend\app\schemas\group.py`

```python

```

## 📄 `backend\app\schemas\post.py`

```python

```

## 📄 `backend\app\schemas\schedule.py`

```python

```

## 📄 `backend\app\schemas\user.py`

```python

```

## 📄 `backend\app\services\auth_service.py`

```python

```

## 📄 `backend\app\services\group_service.py`

```python

```

## 📄 `backend\app\services\post_service.py`

```python

```

## 📄 `backend\app\services\user_service.py`

```python

```

## 📄 `backend\app\services\utils.py`

```python

```

## 📄 `backend\app\utils\datetime.py`

```python

```

## 📄 `backend\app\utils\hashing.py`

```python

```

## 📄 `backend\app\utils\id_generator.py`

```python

```

## 📄 `backend\tests\conftest.py`

```python

```

## 📄 `backend\tests\test_posts.py`

```python

```

## 📄 `backend\tests\test_users.py`

```python

```

## 📄 `frontend\.env.production`

```
NEXT_PUBLIC_API_URL=https://bookverse-backend.onrender.com
NODE_VERSION=18.17.1
PORT=3000
```

## 📄 `frontend\next-env.d.ts`

```typescript
/// <reference types="next" />
/// <reference types="next/image-types/global" />

// NOTE: This file should not be edited
// see https://nextjs.org/docs/basic-features/typescript for more information.

```

## 📄 `frontend\package-lock.json`

```json
{
    "name": "bookverse-frontend",
    "version": "1.0.0",
    "lockfileVersion": 3,
    "requires": true,
    "packages": {
        "": {
            "name": "bookverse-frontend",
            "version": "1.0.0",
            "dependencies": {
                "next": "14.1.0",
                "react": "^18.2.0",
                "react-dom": "^18.2.0"
            },
            "devDependencies": {
                "@types/node": "22.15.14",
                "@types/react": "19.1.3",
                "autoprefixer": "^10.4.13",
                "postcss": "^8.4.21",
                "tailwindcss": "^3.3.2",
                "typescript": "^5.0.0"
            }
        },
        "node_modules/@alloc/quick-lru": {
            "version": "5.2.0",
            "resolved": "https://registry.npmjs.org/@alloc/quick-lru/-/quick-lru-5.2.0.tgz",
            "integrity": "sha512-UrcABB+4bUrFABwbluTIBErXwvbsU/V7TZWfmbgJfbkwiBuziS9gxdODUyuiecfdGQ85jglMW6juS3+z5TsKLw==",
            "dev": true,
            "license": "MIT",
            "engines": {
                "node": ">=10"
            },
            "funding": {
                "url": "https://github.com/sponsors/sindresorhus"
            }
        },
        "node_modules/@isaacs/cliui": {
            "version": "8.0.2",
            "resolved": "https://registry.npmjs.org/@isaacs/cliui/-/cliui-8.0.2.tgz",
            "integrity": "sha512-O8jcjabXaleOG9DQ0+ARXWZBTfnP4WNAqzuiJK7ll44AmxGKv/J2M4TPjxjY3znBCfvBXFzucm1twdyFybFqEA==",
            "dev": true,
            "license": "ISC",
            "dependencies": {
                "string-width": "^5.1.2",
                "string-width-cjs": "npm:string-width@^4.2.0",
                "strip-ansi": "^7.0.1",
                "strip-ansi-cjs": "npm:strip-ansi@^6.0.1",
                "wrap-ansi": "^8.1.0",
                "wrap-ansi-cjs": "npm:wrap-ansi@^7.0.0"
            },
            "engines": {
                "node": ">=12"
            }
        },
        "node_modules/@jridgewell/gen-mapping": {
            "version": "0.3.8",
            "resolved": "https://registry.npmjs.org/@jridgewell/gen-mapping/-/gen-mapping-0.3.8.tgz",
            "integrity": "sha512-imAbBGkb+ebQyxKgzv5Hu2nmROxoDOXHh80evxdoXNOrvAnVx7zimzc1Oo5h9RlfV4vPXaE2iM5pOFbvOCClWA==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "@jridgewell/set-array": "^1.2.1",
                "@jridgewell/sourcemap-codec": "^1.4.10",
                "@jridgewell/trace-mapping": "^0.3.24"
            },
            "engines": {
                "node": ">=6.0.0"
            }
        },
        "node_modules/@jridgewell/resolve-uri": {
            "version": "3.1.2",
            "resolved": "https://registry.npmjs.org/@jridgewell/resolve-uri/-/resolve-uri-3.1.2.tgz",
            "integrity": "sha512-bRISgCIjP20/tbWSPWMEi54QVPRZExkuD9lJL+UIxUKtwVJA8wW1Trb1jMs1RFXo1CBTNZ/5hpC9QvmKWdopKw==",
            "dev": true,
            "license": "MIT",
            "engines": {
                "node": ">=6.0.0"
            }
        },
        "node_modules/@jridgewell/set-array": {
            "version": "1.2.1",
            "resolved": "https://registry.npmjs.org/@jridgewell/set-array/-/set-array-1.2.1.tgz",
            "integrity": "sha512-R8gLRTZeyp03ymzP/6Lil/28tGeGEzhx1q2k703KGWRAI1VdvPIXdG70VJc2pAMw3NA6JKL5hhFu1sJX0Mnn/A==",
            "dev": true,
            "license": "MIT",
            "engines": {
                "node": ">=6.0.0"
            }
        },
        "node_modules/@jridgewell/sourcemap-codec": {
            "version": "1.5.0",
            "resolved": "https://registry.npmjs.org/@jridgewell/sourcemap-codec/-/sourcemap-codec-1.5.0.tgz",
            "integrity": "sha512-gv3ZRaISU3fjPAgNsriBRqGWQL6quFx04YMPW/zD8XMLsU32mhCCbfbO6KZFLjvYpCZ8zyDEgqsgf+PwPaM7GQ==",
            "dev": true,
            "license": "MIT"
        },
        "node_modules/@jridgewell/trace-mapping": {
            "version": "0.3.25",
            "resolved": "https://registry.npmjs.org/@jridgewell/trace-mapping/-/trace-mapping-0.3.25.tgz",
            "integrity": "sha512-vNk6aEwybGtawWmy/PzwnGDOjCkLWSD2wqvjGGAgOAwCGWySYXfYoxt00IJkTF+8Lb57DwOb3Aa0o9CApepiYQ==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "@jridgewell/resolve-uri": "^3.1.0",
                "@jridgewell/sourcemap-codec": "^1.4.14"
            }
        },
        "node_modules/@next/env": {
            "version": "14.1.0",
            "resolved": "https://registry.npmjs.org/@next/env/-/env-14.1.0.tgz",
            "integrity": "sha512-Py8zIo+02ht82brwwhTg36iogzFqGLPXlRGKQw5s+qP/kMNc4MAyDeEwBKDijk6zTIbegEgu8Qy7C1LboslQAw==",
            "license": "MIT"
        },
        "node_modules/@next/swc-darwin-arm64": {
            "version": "14.1.0",
            "resolved": "https://registry.npmjs.org/@next/swc-darwin-arm64/-/swc-darwin-arm64-14.1.0.tgz",
            "integrity": "sha512-nUDn7TOGcIeyQni6lZHfzNoo9S0euXnu0jhsbMOmMJUBfgsnESdjN97kM7cBqQxZa8L/bM9om/S5/1dzCrW6wQ==",
            "cpu": [
                "arm64"
            ],
            "license": "MIT",
            "optional": true,
            "os": [
                "darwin"
            ],
            "engines": {
                "node": ">= 10"
            }
        },
        "node_modules/@next/swc-darwin-x64": {
            "version": "14.1.0",
            "resolved": "https://registry.npmjs.org/@next/swc-darwin-x64/-/swc-darwin-x64-14.1.0.tgz",
            "integrity": "sha512-1jgudN5haWxiAl3O1ljUS2GfupPmcftu2RYJqZiMJmmbBT5M1XDffjUtRUzP4W3cBHsrvkfOFdQ71hAreNQP6g==",
            "cpu": [
                "x64"
            ],
            "license": "MIT",
            "optional": true,
            "os": [
                "darwin"
            ],
            "engines": {
                "node": ">= 10"
            }
        },
        "node_modules/@next/swc-linux-arm64-gnu": {
            "version": "14.1.0",
            "resolved": "https://registry.npmjs.org/@next/swc-linux-arm64-gnu/-/swc-linux-arm64-gnu-14.1.0.tgz",
            "integrity": "sha512-RHo7Tcj+jllXUbK7xk2NyIDod3YcCPDZxj1WLIYxd709BQ7WuRYl3OWUNG+WUfqeQBds6kvZYlc42NJJTNi4tQ==",
            "cpu": [
                "arm64"
            ],
            "license": "MIT",
            "optional": true,
            "os": [
                "linux"
            ],
            "engines": {
                "node": ">= 10"
            }
        },
        "node_modules/@next/swc-linux-arm64-musl": {
            "version": "14.1.0",
            "resolved": "https://registry.npmjs.org/@next/swc-linux-arm64-musl/-/swc-linux-arm64-musl-14.1.0.tgz",
            "integrity": "sha512-v6kP8sHYxjO8RwHmWMJSq7VZP2nYCkRVQ0qolh2l6xroe9QjbgV8siTbduED4u0hlk0+tjS6/Tuy4n5XCp+l6g==",
            "cpu": [
                "arm64"
            ],
            "license": "MIT",
            "optional": true,
            "os": [
                "linux"
            ],
            "engines": {
                "node": ">= 10"
            }
        },
        "node_modules/@next/swc-linux-x64-gnu": {
            "version": "14.1.0",
            "resolved": "https://registry.npmjs.org/@next/swc-linux-x64-gnu/-/swc-linux-x64-gnu-14.1.0.tgz",
            "integrity": "sha512-zJ2pnoFYB1F4vmEVlb/eSe+VH679zT1VdXlZKX+pE66grOgjmKJHKacf82g/sWE4MQ4Rk2FMBCRnX+l6/TVYzQ==",
            "cpu": [
                "x64"
            ],
            "license": "MIT",
            "optional": true,
            "os": [
                "linux"
            ],
            "engines": {
                "node": ">= 10"
            }
        },
        "node_modules/@next/swc-linux-x64-musl": {
            "version": "14.1.0",
            "resolved": "https://registry.npmjs.org/@next/swc-linux-x64-musl/-/swc-linux-x64-musl-14.1.0.tgz",
            "integrity": "sha512-rbaIYFt2X9YZBSbH/CwGAjbBG2/MrACCVu2X0+kSykHzHnYH5FjHxwXLkcoJ10cX0aWCEynpu+rP76x0914atg==",
            "cpu": [
                "x64"
            ],
            "license": "MIT",
            "optional": true,
            "os": [
                "linux"
            ],
            "engines": {
                "node": ">= 10"
            }
        },
        "node_modules/@next/swc-win32-arm64-msvc": {
            "version": "14.1.0",
            "resolved": "https://registry.npmjs.org/@next/swc-win32-arm64-msvc/-/swc-win32-arm64-msvc-14.1.0.tgz",
            "integrity": "sha512-o1N5TsYc8f/HpGt39OUQpQ9AKIGApd3QLueu7hXk//2xq5Z9OxmV6sQfNp8C7qYmiOlHYODOGqNNa0e9jvchGQ==",
            "cpu": [
                "arm64"
            ],
            "license": "MIT",
            "optional": true,
            "os": [
                "win32"
            ],
            "engines": {
                "node": ">= 10"
            }
        },
        "node_modules/@next/swc-win32-ia32-msvc": {
            "version": "14.1.0",
            "resolved": "https://registry.npmjs.org/@next/swc-win32-ia32-msvc/-/swc-win32-ia32-msvc-14.1.0.tgz",
            "integrity": "sha512-XXIuB1DBRCFwNO6EEzCTMHT5pauwaSj4SWs7CYnME57eaReAKBXCnkUE80p/pAZcewm7hs+vGvNqDPacEXHVkw==",
            "cpu": [
                "ia32"
            ],
            "license": "MIT",
            "optional": true,
            "os": [
                "win32"
            ],
            "engines": {
                "node": ">= 10"
            }
        },
        "node_modules/@next/swc-win32-x64-msvc": {
            "version": "14.1.0",
            "resolved": "https://registry.npmjs.org/@next/swc-win32-x64-msvc/-/swc-win32-x64-msvc-14.1.0.tgz",
            "integrity": "sha512-9WEbVRRAqJ3YFVqEZIxUqkiO8l1nool1LmNxygr5HWF8AcSYsEpneUDhmjUVJEzO2A04+oPtZdombzzPPkTtgg==",
            "cpu": [
                "x64"
            ],
            "license": "MIT",
            "optional": true,
            "os": [
                "win32"
            ],
            "engines": {
                "node": ">= 10"
            }
        },
        "node_modules/@nodelib/fs.scandir": {
            "version": "2.1.5",
            "resolved": "https://registry.npmjs.org/@nodelib/fs.scandir/-/fs.scandir-2.1.5.tgz",
            "integrity": "sha512-vq24Bq3ym5HEQm2NKCr3yXDwjc7vTsEThRDnkp2DK9p1uqLR+DHurm/NOTo0KG7HYHU7eppKZj3MyqYuMBf62g==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "@nodelib/fs.stat": "2.0.5",
                "run-parallel": "^1.1.9"
            },
            "engines": {
                "node": ">= 8"
            }
        },
        "node_modules/@nodelib/fs.stat": {
            "version": "2.0.5",
            "resolved": "https://registry.npmjs.org/@nodelib/fs.stat/-/fs.stat-2.0.5.tgz",
            "integrity": "sha512-RkhPPp2zrqDAQA/2jNhnztcPAlv64XdhIp7a7454A5ovI7Bukxgt7MX7udwAu3zg1DcpPU0rz3VV1SeaqvY4+A==",
            "dev": true,
            "license": "MIT",
            "engines": {
                "node": ">= 8"
            }
        },
        "node_modules/@nodelib/fs.walk": {
            "version": "1.2.8",
            "resolved": "https://registry.npmjs.org/@nodelib/fs.walk/-/fs.walk-1.2.8.tgz",
            "integrity": "sha512-oGB+UxlgWcgQkgwo8GcEGwemoTFt3FIO9ababBmaGwXIoBKZ+GTy0pP185beGg7Llih/NSHSV2XAs1lnznocSg==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "@nodelib/fs.scandir": "2.1.5",
                "fastq": "^1.6.0"
            },
            "engines": {
                "node": ">= 8"
            }
        },
        "node_modules/@pkgjs/parseargs": {
            "version": "0.11.0",
            "resolved": "https://registry.npmjs.org/@pkgjs/parseargs/-/parseargs-0.11.0.tgz",
            "integrity": "sha512-+1VkjdD0QBLPodGrJUeqarH8VAIvQODIbwh9XpP5Syisf7YoQgsJKPNFoqqLQlu+VQ/tVSshMR6loPMn8U+dPg==",
            "dev": true,
            "license": "MIT",
            "optional": true,
            "engines": {
                "node": ">=14"
            }
        },
        "node_modules/@swc/helpers": {
            "version": "0.5.2",
            "resolved": "https://registry.npmjs.org/@swc/helpers/-/helpers-0.5.2.tgz",
            "integrity": "sha512-E4KcWTpoLHqwPHLxidpOqQbcrZVgi0rsmmZXUle1jXmJfuIf/UWpczUJ7MZZ5tlxytgJXyp0w4PGkkeLiuIdZw==",
            "license": "Apache-2.0",
            "dependencies": {
                "tslib": "^2.4.0"
            }
        },
        "node_modules/@types/node": {
            "version": "22.15.14",
            "resolved": "https://registry.npmjs.org/@types/node/-/node-22.15.14.tgz",
            "integrity": "sha512-BL1eyu/XWsFGTtDWOYULQEs4KR0qdtYfCxYAUYRoB7JP7h9ETYLgQTww6kH8Sj2C0pFGgrpM0XKv6/kbIzYJ1g==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "undici-types": "~6.21.0"
            }
        },
        "node_modules/@types/react": {
            "version": "19.1.3",
            "resolved": "https://registry.npmjs.org/@types/react/-/react-19.1.3.tgz",
            "integrity": "sha512-dLWQ+Z0CkIvK1J8+wrDPwGxEYFA4RAyHoZPxHVGspYmFVnwGSNT24cGIhFJrtfRnWVuW8X7NO52gCXmhkVUWGQ==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "csstype": "^3.0.2"
            }
        },
        "node_modules/ansi-regex": {
            "version": "6.1.0",
            "resolved": "https://registry.npmjs.org/ansi-regex/-/ansi-regex-6.1.0.tgz",
            "integrity": "sha512-7HSX4QQb4CspciLpVFwyRe79O3xsIZDDLER21kERQ71oaPodF8jL725AgJMFAYbooIqolJoRLuM81SpeUkpkvA==",
            "dev": true,
            "license": "MIT",
            "engines": {
                "node": ">=12"
            },
            "funding": {
                "url": "https://github.com/chalk/ansi-regex?sponsor=1"
            }
        },
        "node_modules/ansi-styles": {
            "version": "6.2.1",
            "resolved": "https://registry.npmjs.org/ansi-styles/-/ansi-styles-6.2.1.tgz",
            "integrity": "sha512-bN798gFfQX+viw3R7yrGWRqnrN2oRkEkUjjl4JNn4E8GxxbjtG3FbrEIIY3l8/hrwUwIeCZvi4QuOTP4MErVug==",
            "dev": true,
            "license": "MIT",
            "engines": {
                "node": ">=12"
            },
            "funding": {
                "url": "https://github.com/chalk/ansi-styles?sponsor=1"
            }
        },
        "node_modules/any-promise": {
            "version": "1.3.0",
            "resolved": "https://registry.npmjs.org/any-promise/-/any-promise-1.3.0.tgz",
            "integrity": "sha512-7UvmKalWRt1wgjL1RrGxoSJW/0QZFIegpeGvZG9kjp8vrRu55XTHbwnqq2GpXm9uLbcuhxm3IqX9OB4MZR1b2A==",
            "dev": true,
            "license": "MIT"
        },
        "node_modules/anymatch": {
            "version": "3.1.3",
            "resolved": "https://registry.npmjs.org/anymatch/-/anymatch-3.1.3.tgz",
            "integrity": "sha512-KMReFUr0B4t+D+OBkjR3KYqvocp2XaSzO55UcB6mgQMd3KbcE+mWTyvVV7D/zsdEbNnV6acZUutkiHQXvTr1Rw==",
            "dev": true,
            "license": "ISC",
            "dependencies": {
                "normalize-path": "^3.0.0",
                "picomatch": "^2.0.4"
            },
            "engines": {
                "node": ">= 8"
            }
        },
        "node_modules/arg": {
            "version": "5.0.2",
            "resolved": "https://registry.npmjs.org/arg/-/arg-5.0.2.tgz",
            "integrity": "sha512-PYjyFOLKQ9y57JvQ6QLo8dAgNqswh8M1RMJYdQduT6xbWSgK36P/Z/v+p888pM69jMMfS8Xd8F6I1kQ/I9HUGg==",
            "dev": true,
            "license": "MIT"
        },
        "node_modules/autoprefixer": {
            "version": "10.4.21",
            "resolved": "https://registry.npmjs.org/autoprefixer/-/autoprefixer-10.4.21.tgz",
            "integrity": "sha512-O+A6LWV5LDHSJD3LjHYoNi4VLsj/Whi7k6zG12xTYaU4cQ8oxQGckXNX8cRHK5yOZ/ppVHe0ZBXGzSV9jXdVbQ==",
            "dev": true,
            "funding": [
                {
                    "type": "opencollective",
                    "url": "https://opencollective.com/postcss/"
                },
                {
                    "type": "tidelift",
                    "url": "https://tidelift.com/funding/github/npm/autoprefixer"
                },
                {
                    "type": "github",
                    "url": "https://github.com/sponsors/ai"
                }
            ],
            "license": "MIT",
            "dependencies": {
                "browserslist": "^4.24.4",
                "caniuse-lite": "^1.0.30001702",
                "fraction.js": "^4.3.7",
                "normalize-range": "^0.1.2",
                "picocolors": "^1.1.1",
                "postcss-value-parser": "^4.2.0"
            },
            "bin": {
                "autoprefixer": "bin/autoprefixer"
            },
            "engines": {
                "node": "^10 || ^12 || >=14"
            },
            "peerDependencies": {
                "postcss": "^8.1.0"
            }
        },
        "node_modules/balanced-match": {
            "version": "1.0.2",
            "resolved": "https://registry.npmjs.org/balanced-match/-/balanced-match-1.0.2.tgz",
            "integrity": "sha512-3oSeUO0TMV67hN1AmbXsK4yaqU7tjiHlbxRDZOpH0KW9+CeX4bRAaX0Anxt0tx2MrpRpWwQaPwIlISEJhYU5Pw==",
            "dev": true,
            "license": "MIT"
        },
        "node_modules/binary-extensions": {
            "version": "2.3.0",
            "resolved": "https://registry.npmjs.org/binary-extensions/-/binary-extensions-2.3.0.tgz",
            "integrity": "sha512-Ceh+7ox5qe7LJuLHoY0feh3pHuUDHAcRUeyL2VYghZwfpkNIy/+8Ocg0a3UuSoYzavmylwuLWQOf3hl0jjMMIw==",
            "dev": true,
            "license": "MIT",
            "engines": {
                "node": ">=8"
            },
            "funding": {
                "url": "https://github.com/sponsors/sindresorhus"
            }
        },
        "node_modules/brace-expansion": {
            "version": "2.0.1",
            "resolved": "https://registry.npmjs.org/brace-expansion/-/brace-expansion-2.0.1.tgz",
            "integrity": "sha512-XnAIvQ8eM+kC6aULx6wuQiwVsnzsi9d3WxzV3FpWTGA19F621kwdbsAcFKXgKUHZWsy+mY6iL1sHTxWEFCytDA==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "balanced-match": "^1.0.0"
            }
        },
        "node_modules/braces": {
            "version": "3.0.3",
            "resolved": "https://registry.npmjs.org/braces/-/braces-3.0.3.tgz",
            "integrity": "sha512-yQbXgO/OSZVD2IsiLlro+7Hf6Q18EJrKSEsdoMzKePKXct3gvD8oLcOQdIzGupr5Fj+EDe8gO/lxc1BzfMpxvA==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "fill-range": "^7.1.1"
            },
            "engines": {
                "node": ">=8"
            }
        },
        "node_modules/browserslist": {
            "version": "4.24.5",
            "resolved": "https://registry.npmjs.org/browserslist/-/browserslist-4.24.5.tgz",
            "integrity": "sha512-FDToo4Wo82hIdgc1CQ+NQD0hEhmpPjrZ3hiUgwgOG6IuTdlpr8jdjyG24P6cNP1yJpTLzS5OcGgSw0xmDU1/Tw==",
            "dev": true,
            "funding": [
                {
                    "type": "opencollective",
                    "url": "https://opencollective.com/browserslist"
                },
                {
                    "type": "tidelift",
                    "url": "https://tidelift.com/funding/github/npm/browserslist"
                },
                {
                    "type": "github",
                    "url": "https://github.com/sponsors/ai"
                }
            ],
            "license": "MIT",
            "dependencies": {
                "caniuse-lite": "^1.0.30001716",
                "electron-to-chromium": "^1.5.149",
                "node-releases": "^2.0.19",
                "update-browserslist-db": "^1.1.3"
            },
            "bin": {
                "browserslist": "cli.js"
            },
            "engines": {
                "node": "^6 || ^7 || ^8 || ^9 || ^10 || ^11 || ^12 || >=13.7"
            }
        },
        "node_modules/busboy": {
            "version": "1.6.0",
            "resolved": "https://registry.npmjs.org/busboy/-/busboy-1.6.0.tgz",
            "integrity": "sha512-8SFQbg/0hQ9xy3UNTB0YEnsNBbWfhf7RtnzpL7TkBiTBRfrQ9Fxcnz7VJsleJpyp6rVLvXiuORqjlHi5q+PYuA==",
            "dependencies": {
                "streamsearch": "^1.1.0"
            },
            "engines": {
                "node": ">=10.16.0"
            }
        },
        "node_modules/camelcase-css": {
            "version": "2.0.1",
            "resolved": "https://registry.npmjs.org/camelcase-css/-/camelcase-css-2.0.1.tgz",
            "integrity": "sha512-QOSvevhslijgYwRx6Rv7zKdMF8lbRmx+uQGx2+vDc+KI/eBnsy9kit5aj23AgGu3pa4t9AgwbnXWqS+iOY+2aA==",
            "dev": true,
            "license": "MIT",
            "engines": {
                "node": ">= 6"
            }
        },
        "node_modules/caniuse-lite": {
            "version": "1.0.30001717",
            "resolved": "https://registry.npmjs.org/caniuse-lite/-/caniuse-lite-1.0.30001717.tgz",
            "integrity": "sha512-auPpttCq6BDEG8ZAuHJIplGw6GODhjw+/11e7IjpnYCxZcW/ONgPs0KVBJ0d1bY3e2+7PRe5RCLyP+PfwVgkYw==",
            "funding": [
                {
                    "type": "opencollective",
                    "url": "https://opencollective.com/browserslist"
                },
                {
                    "type": "tidelift",
                    "url": "https://tidelift.com/funding/github/npm/caniuse-lite"
                },
                {
                    "type": "github",
                    "url": "https://github.com/sponsors/ai"
                }
            ],
            "license": "CC-BY-4.0"
        },
        "node_modules/chokidar": {
            "version": "3.6.0",
            "resolved": "https://registry.npmjs.org/chokidar/-/chokidar-3.6.0.tgz",
            "integrity": "sha512-7VT13fmjotKpGipCW9JEQAusEPE+Ei8nl6/g4FBAmIm0GOOLMua9NDDo/DWp0ZAxCr3cPq5ZpBqmPAQgDda2Pw==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "anymatch": "~3.1.2",
                "braces": "~3.0.2",
                "glob-parent": "~5.1.2",
                "is-binary-path": "~2.1.0",
                "is-glob": "~4.0.1",
                "normalize-path": "~3.0.0",
                "readdirp": "~3.6.0"
            },
            "engines": {
                "node": ">= 8.10.0"
            },
            "funding": {
                "url": "https://paulmillr.com/funding/"
            },
            "optionalDependencies": {
                "fsevents": "~2.3.2"
            }
        },
        "node_modules/chokidar/node_modules/glob-parent": {
            "version": "5.1.2",
            "resolved": "https://registry.npmjs.org/glob-parent/-/glob-parent-5.1.2.tgz",
            "integrity": "sha512-AOIgSQCepiJYwP3ARnGx+5VnTu2HBYdzbGP45eLw1vr3zB3vZLeyed1sC9hnbcOc9/SrMyM5RPQrkGz4aS9Zow==",
            "dev": true,
            "license": "ISC",
            "dependencies": {
                "is-glob": "^4.0.1"
            },
            "engines": {
                "node": ">= 6"
            }
        },
        "node_modules/client-only": {
            "version": "0.0.1",
            "resolved": "https://registry.npmjs.org/client-only/-/client-only-0.0.1.tgz",
            "integrity": "sha512-IV3Ou0jSMzZrd3pZ48nLkT9DA7Ag1pnPzaiQhpW7c3RbcqqzvzzVu+L8gfqMp/8IM2MQtSiqaCxrrcfu8I8rMA==",
            "license": "MIT"
        },
        "node_modules/color-convert": {
            "version": "2.0.1",
            "resolved": "https://registry.npmjs.org/color-convert/-/color-convert-2.0.1.tgz",
            "integrity": "sha512-RRECPsj7iu/xb5oKYcsFHSppFNnsj/52OVTRKb4zP5onXwVF3zVmmToNcOfGC+CRDpfK/U584fMg38ZHCaElKQ==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "color-name": "~1.1.4"
            },
            "engines": {
                "node": ">=7.0.0"
            }
        },
        "node_modules/color-name": {
            "version": "1.1.4",
            "resolved": "https://registry.npmjs.org/color-name/-/color-name-1.1.4.tgz",
            "integrity": "sha512-dOy+3AuW3a2wNbZHIuMZpTcgjGuLU/uBL/ubcZF9OXbDo8ff4O8yVp5Bf0efS8uEoYo5q4Fx7dY9OgQGXgAsQA==",
            "dev": true,
            "license": "MIT"
        },
        "node_modules/commander": {
            "version": "4.1.1",
            "resolved": "https://registry.npmjs.org/commander/-/commander-4.1.1.tgz",
            "integrity": "sha512-NOKm8xhkzAjzFx8B2v5OAHT+u5pRQc2UCa2Vq9jYL/31o2wi9mxBA7LIFs3sV5VSC49z6pEhfbMULvShKj26WA==",
            "dev": true,
            "license": "MIT",
            "engines": {
                "node": ">= 6"
            }
        },
        "node_modules/cross-spawn": {
            "version": "7.0.6",
            "resolved": "https://registry.npmjs.org/cross-spawn/-/cross-spawn-7.0.6.tgz",
            "integrity": "sha512-uV2QOWP2nWzsy2aMp8aRibhi9dlzF5Hgh5SHaB9OiTGEyDTiJJyx0uy51QXdyWbtAHNua4XJzUKca3OzKUd3vA==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "path-key": "^3.1.0",
                "shebang-command": "^2.0.0",
                "which": "^2.0.1"
            },
            "engines": {
                "node": ">= 8"
            }
        },
        "node_modules/cssesc": {
            "version": "3.0.0",
            "resolved": "https://registry.npmjs.org/cssesc/-/cssesc-3.0.0.tgz",
            "integrity": "sha512-/Tb/JcjK111nNScGob5MNtsntNM1aCNUDipB/TkwZFhyDrrE47SOx/18wF2bbjgc3ZzCSKW1T5nt5EbFoAz/Vg==",
            "dev": true,
            "license": "MIT",
            "bin": {
                "cssesc": "bin/cssesc"
            },
            "engines": {
                "node": ">=4"
            }
        },
        "node_modules/csstype": {
            "version": "3.1.3",
            "resolved": "https://registry.npmjs.org/csstype/-/csstype-3.1.3.tgz",
            "integrity": "sha512-M1uQkMl8rQK/szD0LNhtqxIPLpimGm8sOBwU7lLnCpSbTyY3yeU1Vc7l4KT5zT4s/yOxHH5O7tIuuLOCnLADRw==",
            "dev": true,
            "license": "MIT"
        },
        "node_modules/didyoumean": {
            "version": "1.2.2",
            "resolved": "https://registry.npmjs.org/didyoumean/-/didyoumean-1.2.2.tgz",
            "integrity": "sha512-gxtyfqMg7GKyhQmb056K7M3xszy/myH8w+B4RT+QXBQsvAOdc3XymqDDPHx1BgPgsdAA5SIifona89YtRATDzw==",
            "dev": true,
            "license": "Apache-2.0"
        },
        "node_modules/dlv": {
            "version": "1.1.3",
            "resolved": "https://registry.npmjs.org/dlv/-/dlv-1.1.3.tgz",
            "integrity": "sha512-+HlytyjlPKnIG8XuRG8WvmBP8xs8P71y+SKKS6ZXWoEgLuePxtDoUEiH7WkdePWrQ5JBpE6aoVqfZfJUQkjXwA==",
            "dev": true,
            "license": "MIT"
        },
        "node_modules/eastasianwidth": {
            "version": "0.2.0",
            "resolved": "https://registry.npmjs.org/eastasianwidth/-/eastasianwidth-0.2.0.tgz",
            "integrity": "sha512-I88TYZWc9XiYHRQ4/3c5rjjfgkjhLyW2luGIheGERbNQ6OY7yTybanSpDXZa8y7VUP9YmDcYa+eyq4ca7iLqWA==",
            "dev": true,
            "license": "MIT"
        },
        "node_modules/electron-to-chromium": {
            "version": "1.5.150",
            "resolved": "https://registry.npmjs.org/electron-to-chromium/-/electron-to-chromium-1.5.150.tgz",
            "integrity": "sha512-rOOkP2ZUMx1yL4fCxXQKDHQ8ZXwisb2OycOQVKHgvB3ZI4CvehOd4y2tfnnLDieJ3Zs1RL1Dlp3cMkyIn7nnXA==",
            "dev": true,
            "license": "ISC"
        },
        "node_modules/emoji-regex": {
            "version": "9.2.2",
            "resolved": "https://registry.npmjs.org/emoji-regex/-/emoji-regex-9.2.2.tgz",
            "integrity": "sha512-L18DaJsXSUk2+42pv8mLs5jJT2hqFkFE4j21wOmgbUqsZ2hL72NsUU785g9RXgo3s0ZNgVl42TiHp3ZtOv/Vyg==",
            "dev": true,
            "license": "MIT"
        },
        "node_modules/escalade": {
            "version": "3.2.0",
            "resolved": "https://registry.npmjs.org/escalade/-/escalade-3.2.0.tgz",
            "integrity": "sha512-WUj2qlxaQtO4g6Pq5c29GTcWGDyd8itL8zTlipgECz3JesAiiOKotd8JU6otB3PACgG6xkJUyVhboMS+bje/jA==",
            "dev": true,
            "license": "MIT",
            "engines": {
                "node": ">=6"
            }
        },
        "node_modules/fast-glob": {
            "version": "3.3.3",
            "resolved": "https://registry.npmjs.org/fast-glob/-/fast-glob-3.3.3.tgz",
            "integrity": "sha512-7MptL8U0cqcFdzIzwOTHoilX9x5BrNqye7Z/LuC7kCMRio1EMSyqRK3BEAUD7sXRq4iT4AzTVuZdhgQ2TCvYLg==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "@nodelib/fs.stat": "^2.0.2",
                "@nodelib/fs.walk": "^1.2.3",
                "glob-parent": "^5.1.2",
                "merge2": "^1.3.0",
                "micromatch": "^4.0.8"
            },
            "engines": {
                "node": ">=8.6.0"
            }
        },
        "node_modules/fast-glob/node_modules/glob-parent": {
            "version": "5.1.2",
            "resolved": "https://registry.npmjs.org/glob-parent/-/glob-parent-5.1.2.tgz",
            "integrity": "sha512-AOIgSQCepiJYwP3ARnGx+5VnTu2HBYdzbGP45eLw1vr3zB3vZLeyed1sC9hnbcOc9/SrMyM5RPQrkGz4aS9Zow==",
            "dev": true,
            "license": "ISC",
            "dependencies": {
                "is-glob": "^4.0.1"
            },
            "engines": {
                "node": ">= 6"
            }
        },
        "node_modules/fastq": {
            "version": "1.19.1",
            "resolved": "https://registry.npmjs.org/fastq/-/fastq-1.19.1.tgz",
            "integrity": "sha512-GwLTyxkCXjXbxqIhTsMI2Nui8huMPtnxg7krajPJAjnEG/iiOS7i+zCtWGZR9G0NBKbXKh6X9m9UIsYX/N6vvQ==",
            "dev": true,
            "license": "ISC",
            "dependencies": {
                "reusify": "^1.0.4"
            }
        },
        "node_modules/fill-range": {
            "version": "7.1.1",
            "resolved": "https://registry.npmjs.org/fill-range/-/fill-range-7.1.1.tgz",
            "integrity": "sha512-YsGpe3WHLK8ZYi4tWDg2Jy3ebRz2rXowDxnld4bkQB00cc/1Zw9AWnC0i9ztDJitivtQvaI9KaLyKrc+hBW0yg==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "to-regex-range": "^5.0.1"
            },
            "engines": {
                "node": ">=8"
            }
        },
        "node_modules/foreground-child": {
            "version": "3.3.1",
            "resolved": "https://registry.npmjs.org/foreground-child/-/foreground-child-3.3.1.tgz",
            "integrity": "sha512-gIXjKqtFuWEgzFRJA9WCQeSJLZDjgJUOMCMzxtvFq/37KojM1BFGufqsCy0r4qSQmYLsZYMeyRqzIWOMup03sw==",
            "dev": true,
            "license": "ISC",
            "dependencies": {
                "cross-spawn": "^7.0.6",
                "signal-exit": "^4.0.1"
            },
            "engines": {
                "node": ">=14"
            },
            "funding": {
                "url": "https://github.com/sponsors/isaacs"
            }
        },
        "node_modules/fraction.js": {
            "version": "4.3.7",
            "resolved": "https://registry.npmjs.org/fraction.js/-/fraction.js-4.3.7.tgz",
            "integrity": "sha512-ZsDfxO51wGAXREY55a7la9LScWpwv9RxIrYABrlvOFBlH/ShPnrtsXeuUIfXKKOVicNxQ+o8JTbJvjS4M89yew==",
            "dev": true,
            "license": "MIT",
            "engines": {
                "node": "*"
            },
            "funding": {
                "type": "patreon",
                "url": "https://github.com/sponsors/rawify"
            }
        },
        "node_modules/fsevents": {
            "version": "2.3.3",
            "resolved": "https://registry.npmjs.org/fsevents/-/fsevents-2.3.3.tgz",
            "integrity": "sha512-5xoDfX+fL7faATnagmWPpbFtwh/R77WmMMqqHGS65C3vvB0YHrgF+B1YmZ3441tMj5n63k0212XNoJwzlhffQw==",
            "dev": true,
            "hasInstallScript": true,
            "license": "MIT",
            "optional": true,
            "os": [
                "darwin"
            ],
            "engines": {
                "node": "^8.16.0 || ^10.6.0 || >=11.0.0"
            }
        },
        "node_modules/function-bind": {
            "version": "1.1.2",
            "resolved": "https://registry.npmjs.org/function-bind/-/function-bind-1.1.2.tgz",
            "integrity": "sha512-7XHNxH7qX9xG5mIwxkhumTox/MIRNcOgDrxWsMt2pAr23WHp6MrRlN7FBSFpCpr+oVO0F744iUgR82nJMfG2SA==",
            "dev": true,
            "license": "MIT",
            "funding": {
                "url": "https://github.com/sponsors/ljharb"
            }
        },
        "node_modules/glob": {
            "version": "10.4.5",
            "resolved": "https://registry.npmjs.org/glob/-/glob-10.4.5.tgz",
            "integrity": "sha512-7Bv8RF0k6xjo7d4A/PxYLbUCfb6c+Vpd2/mB2yRDlew7Jb5hEXiCD9ibfO7wpk8i4sevK6DFny9h7EYbM3/sHg==",
            "dev": true,
            "license": "ISC",
            "dependencies": {
                "foreground-child": "^3.1.0",
                "jackspeak": "^3.1.2",
                "minimatch": "^9.0.4",
                "minipass": "^7.1.2",
                "package-json-from-dist": "^1.0.0",
                "path-scurry": "^1.11.1"
            },
            "bin": {
                "glob": "dist/esm/bin.mjs"
            },
            "funding": {
                "url": "https://github.com/sponsors/isaacs"
            }
        },
        "node_modules/glob-parent": {
            "version": "6.0.2",
            "resolved": "https://registry.npmjs.org/glob-parent/-/glob-parent-6.0.2.tgz",
            "integrity": "sha512-XxwI8EOhVQgWp6iDL+3b0r86f4d6AX6zSU55HfB4ydCEuXLXc5FcYeOu+nnGftS4TEju/11rt4KJPTMgbfmv4A==",
            "dev": true,
            "license": "ISC",
            "dependencies": {
                "is-glob": "^4.0.3"
            },
            "engines": {
                "node": ">=10.13.0"
            }
        },
        "node_modules/graceful-fs": {
            "version": "4.2.11",
            "resolved": "https://registry.npmjs.org/graceful-fs/-/graceful-fs-4.2.11.tgz",
            "integrity": "sha512-RbJ5/jmFcNNCcDV5o9eTnBLJ/HszWV0P73bc+Ff4nS/rJj+YaS6IGyiOL0VoBYX+l1Wrl3k63h/KrH+nhJ0XvQ==",
            "license": "ISC"
        },
        "node_modules/hasown": {
            "version": "2.0.2",
            "resolved": "https://registry.npmjs.org/hasown/-/hasown-2.0.2.tgz",
            "integrity": "sha512-0hJU9SCPvmMzIBdZFqNPXWa6dqh7WdH0cII9y+CyS8rG3nL48Bclra9HmKhVVUHyPWNH5Y7xDwAB7bfgSjkUMQ==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "function-bind": "^1.1.2"
            },
            "engines": {
                "node": ">= 0.4"
            }
        },
        "node_modules/is-binary-path": {
            "version": "2.1.0",
            "resolved": "https://registry.npmjs.org/is-binary-path/-/is-binary-path-2.1.0.tgz",
            "integrity": "sha512-ZMERYes6pDydyuGidse7OsHxtbI7WVeUEozgR/g7rd0xUimYNlvZRE/K2MgZTjWy725IfelLeVcEM97mmtRGXw==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "binary-extensions": "^2.0.0"
            },
            "engines": {
                "node": ">=8"
            }
        },
        "node_modules/is-core-module": {
            "version": "2.16.1",
            "resolved": "https://registry.npmjs.org/is-core-module/-/is-core-module-2.16.1.tgz",
            "integrity": "sha512-UfoeMA6fIJ8wTYFEUjelnaGI67v6+N7qXJEvQuIGa99l4xsCruSYOVSQ0uPANn4dAzm8lkYPaKLrrijLq7x23w==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "hasown": "^2.0.2"
            },
            "engines": {
                "node": ">= 0.4"
            },
            "funding": {
                "url": "https://github.com/sponsors/ljharb"
            }
        },
        "node_modules/is-extglob": {
            "version": "2.1.1",
            "resolved": "https://registry.npmjs.org/is-extglob/-/is-extglob-2.1.1.tgz",
            "integrity": "sha512-SbKbANkN603Vi4jEZv49LeVJMn4yGwsbzZworEoyEiutsN3nJYdbO36zfhGJ6QEDpOZIFkDtnq5JRxmvl3jsoQ==",
            "dev": true,
            "license": "MIT",
            "engines": {
                "node": ">=0.10.0"
            }
        },
        "node_modules/is-fullwidth-code-point": {
            "version": "3.0.0",
            "resolved": "https://registry.npmjs.org/is-fullwidth-code-point/-/is-fullwidth-code-point-3.0.0.tgz",
            "integrity": "sha512-zymm5+u+sCsSWyD9qNaejV3DFvhCKclKdizYaJUuHA83RLjb7nSuGnddCHGv0hk+KY7BMAlsWeK4Ueg6EV6XQg==",
            "dev": true,
            "license": "MIT",
            "engines": {
                "node": ">=8"
            }
        },
        "node_modules/is-glob": {
            "version": "4.0.3",
            "resolved": "https://registry.npmjs.org/is-glob/-/is-glob-4.0.3.tgz",
            "integrity": "sha512-xelSayHH36ZgE7ZWhli7pW34hNbNl8Ojv5KVmkJD4hBdD3th8Tfk9vYasLM+mXWOZhFkgZfxhLSnrwRr4elSSg==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "is-extglob": "^2.1.1"
            },
            "engines": {
                "node": ">=0.10.0"
            }
        },
        "node_modules/is-number": {
            "version": "7.0.0",
            "resolved": "https://registry.npmjs.org/is-number/-/is-number-7.0.0.tgz",
            "integrity": "sha512-41Cifkg6e8TylSpdtTpeLVMqvSBEVzTttHvERD741+pnZ8ANv0004MRL43QKPDlK9cGvNp6NZWZUBlbGXYxxng==",
            "dev": true,
            "license": "MIT",
            "engines": {
                "node": ">=0.12.0"
            }
        },
        "node_modules/isexe": {
            "version": "2.0.0",
            "resolved": "https://registry.npmjs.org/isexe/-/isexe-2.0.0.tgz",
            "integrity": "sha512-RHxMLp9lnKHGHRng9QFhRCMbYAcVpn69smSGcq3f36xjgVVWThj4qqLbTLlq7Ssj8B+fIQ1EuCEGI2lKsyQeIw==",
            "dev": true,
            "license": "ISC"
        },
        "node_modules/jackspeak": {
            "version": "3.4.3",
            "resolved": "https://registry.npmjs.org/jackspeak/-/jackspeak-3.4.3.tgz",
            "integrity": "sha512-OGlZQpz2yfahA/Rd1Y8Cd9SIEsqvXkLVoSw/cgwhnhFMDbsQFeZYoJJ7bIZBS9BcamUW96asq/npPWugM+RQBw==",
            "dev": true,
            "license": "BlueOak-1.0.0",
            "dependencies": {
                "@isaacs/cliui": "^8.0.2"
            },
            "funding": {
                "url": "https://github.com/sponsors/isaacs"
            },
            "optionalDependencies": {
                "@pkgjs/parseargs": "^0.11.0"
            }
        },
        "node_modules/jiti": {
            "version": "1.21.7",
            "resolved": "https://registry.npmjs.org/jiti/-/jiti-1.21.7.tgz",
            "integrity": "sha512-/imKNG4EbWNrVjoNC/1H5/9GFy+tqjGBHCaSsN+P2RnPqjsLmv6UD3Ej+Kj8nBWaRAwyk7kK5ZUc+OEatnTR3A==",
            "dev": true,
            "license": "MIT",
            "bin": {
                "jiti": "bin/jiti.js"
            }
        },
        "node_modules/js-tokens": {
            "version": "4.0.0",
            "resolved": "https://registry.npmjs.org/js-tokens/-/js-tokens-4.0.0.tgz",
            "integrity": "sha512-RdJUflcE3cUzKiMqQgsCu06FPu9UdIJO0beYbPhHN4k6apgJtifcoCtT9bcxOpYBtpD2kCM6Sbzg4CausW/PKQ==",
            "license": "MIT"
        },
        "node_modules/lilconfig": {
            "version": "3.1.3",
            "resolved": "https://registry.npmjs.org/lilconfig/-/lilconfig-3.1.3.tgz",
            "integrity": "sha512-/vlFKAoH5Cgt3Ie+JLhRbwOsCQePABiU3tJ1egGvyQ+33R/vcwM2Zl2QR/LzjsBeItPt3oSVXapn+m4nQDvpzw==",
            "dev": true,
            "license": "MIT",
            "engines": {
                "node": ">=14"
            },
            "funding": {
                "url": "https://github.com/sponsors/antonk52"
            }
        },
        "node_modules/lines-and-columns": {
            "version": "1.2.4",
            "resolved": "https://registry.npmjs.org/lines-and-columns/-/lines-and-columns-1.2.4.tgz",
            "integrity": "sha512-7ylylesZQ/PV29jhEDl3Ufjo6ZX7gCqJr5F7PKrqc93v7fzSymt1BpwEU8nAUXs8qzzvqhbjhK5QZg6Mt/HkBg==",
            "dev": true,
            "license": "MIT"
        },
        "node_modules/loose-envify": {
            "version": "1.4.0",
            "resolved": "https://registry.npmjs.org/loose-envify/-/loose-envify-1.4.0.tgz",
            "integrity": "sha512-lyuxPGr/Wfhrlem2CL/UcnUc1zcqKAImBDzukY7Y5F/yQiNdko6+fRLevlw1HgMySw7f611UIY408EtxRSoK3Q==",
            "license": "MIT",
            "dependencies": {
                "js-tokens": "^3.0.0 || ^4.0.0"
            },
            "bin": {
                "loose-envify": "cli.js"
            }
        },
        "node_modules/lru-cache": {
            "version": "10.4.3",
            "resolved": "https://registry.npmjs.org/lru-cache/-/lru-cache-10.4.3.tgz",
            "integrity": "sha512-JNAzZcXrCt42VGLuYz0zfAzDfAvJWW6AfYlDBQyDV5DClI2m5sAmK+OIO7s59XfsRsWHp02jAJrRadPRGTt6SQ==",
            "dev": true,
            "license": "ISC"
        },
        "node_modules/merge2": {
            "version": "1.4.1",
            "resolved": "https://registry.npmjs.org/merge2/-/merge2-1.4.1.tgz",
            "integrity": "sha512-8q7VEgMJW4J8tcfVPy8g09NcQwZdbwFEqhe/WZkoIzjn/3TGDwtOCYtXGxA3O8tPzpczCCDgv+P2P5y00ZJOOg==",
            "dev": true,
            "license": "MIT",
            "engines": {
                "node": ">= 8"
            }
        },
        "node_modules/micromatch": {
            "version": "4.0.8",
            "resolved": "https://registry.npmjs.org/micromatch/-/micromatch-4.0.8.tgz",
            "integrity": "sha512-PXwfBhYu0hBCPw8Dn0E+WDYb7af3dSLVWKi3HGv84IdF4TyFoC0ysxFd0Goxw7nSv4T/PzEJQxsYsEiFCKo2BA==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "braces": "^3.0.3",
                "picomatch": "^2.3.1"
            },
            "engines": {
                "node": ">=8.6"
            }
        },
        "node_modules/minimatch": {
            "version": "9.0.5",
            "resolved": "https://registry.npmjs.org/minimatch/-/minimatch-9.0.5.tgz",
            "integrity": "sha512-G6T0ZX48xgozx7587koeX9Ys2NYy6Gmv//P89sEte9V9whIapMNF4idKxnW2QtCcLiTWlb/wfCabAtAFWhhBow==",
            "dev": true,
            "license": "ISC",
            "dependencies": {
                "brace-expansion": "^2.0.1"
            },
            "engines": {
                "node": ">=16 || 14 >=14.17"
            },
            "funding": {
                "url": "https://github.com/sponsors/isaacs"
            }
        },
        "node_modules/minipass": {
            "version": "7.1.2",
            "resolved": "https://registry.npmjs.org/minipass/-/minipass-7.1.2.tgz",
            "integrity": "sha512-qOOzS1cBTWYF4BH8fVePDBOO9iptMnGUEZwNc/cMWnTV2nVLZ7VoNWEPHkYczZA0pdoA7dl6e7FL659nX9S2aw==",
            "dev": true,
            "license": "ISC",
            "engines": {
                "node": ">=16 || 14 >=14.17"
            }
        },
        "node_modules/mz": {
            "version": "2.7.0",
            "resolved": "https://registry.npmjs.org/mz/-/mz-2.7.0.tgz",
            "integrity": "sha512-z81GNO7nnYMEhrGh9LeymoE4+Yr0Wn5McHIZMK5cfQCl+NDX08sCZgUc9/6MHni9IWuFLm1Z3HTCXu2z9fN62Q==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "any-promise": "^1.0.0",
                "object-assign": "^4.0.1",
                "thenify-all": "^1.0.0"
            }
        },
        "node_modules/nanoid": {
            "version": "3.3.11",
            "resolved": "https://registry.npmjs.org/nanoid/-/nanoid-3.3.11.tgz",
            "integrity": "sha512-N8SpfPUnUp1bK+PMYW8qSWdl9U+wwNWI4QKxOYDy9JAro3WMX7p2OeVRF9v+347pnakNevPmiHhNmZ2HbFA76w==",
            "funding": [
                {
                    "type": "github",
                    "url": "https://github.com/sponsors/ai"
                }
            ],
            "license": "MIT",
            "bin": {
                "nanoid": "bin/nanoid.cjs"
            },
            "engines": {
                "node": "^10 || ^12 || ^13.7 || ^14 || >=15.0.1"
            }
        },
        "node_modules/next": {
            "version": "14.1.0",
            "resolved": "https://registry.npmjs.org/next/-/next-14.1.0.tgz",
            "integrity": "sha512-wlzrsbfeSU48YQBjZhDzOwhWhGsy+uQycR8bHAOt1LY1bn3zZEcDyHQOEoN3aWzQ8LHCAJ1nqrWCc9XF2+O45Q==",
            "license": "MIT",
            "dependencies": {
                "@next/env": "14.1.0",
                "@swc/helpers": "0.5.2",
                "busboy": "1.6.0",
                "caniuse-lite": "^1.0.30001579",
                "graceful-fs": "^4.2.11",
                "postcss": "8.4.31",
                "styled-jsx": "5.1.1"
            },
            "bin": {
                "next": "dist/bin/next"
            },
            "engines": {
                "node": ">=18.17.0"
            },
            "optionalDependencies": {
                "@next/swc-darwin-arm64": "14.1.0",
                "@next/swc-darwin-x64": "14.1.0",
                "@next/swc-linux-arm64-gnu": "14.1.0",
                "@next/swc-linux-arm64-musl": "14.1.0",
                "@next/swc-linux-x64-gnu": "14.1.0",
                "@next/swc-linux-x64-musl": "14.1.0",
                "@next/swc-win32-arm64-msvc": "14.1.0",
                "@next/swc-win32-ia32-msvc": "14.1.0",
                "@next/swc-win32-x64-msvc": "14.1.0"
            },
            "peerDependencies": {
                "@opentelemetry/api": "^1.1.0",
                "react": "^18.2.0",
                "react-dom": "^18.2.0",
                "sass": "^1.3.0"
            },
            "peerDependenciesMeta": {
                "@opentelemetry/api": {
                    "optional": true
                },
                "sass": {
                    "optional": true
                }
            }
        },
        "node_modules/next/node_modules/postcss": {
            "version": "8.4.31",
            "resolved": "https://registry.npmjs.org/postcss/-/postcss-8.4.31.tgz",
            "integrity": "sha512-PS08Iboia9mts/2ygV3eLpY5ghnUcfLV/EXTOW1E2qYxJKGGBUtNjN76FYHnMs36RmARn41bC0AZmn+rR0OVpQ==",
            "funding": [
                {
                    "type": "opencollective",
                    "url": "https://opencollective.com/postcss/"
                },
                {
                    "type": "tidelift",
                    "url": "https://tidelift.com/funding/github/npm/postcss"
                },
                {
                    "type": "github",
                    "url": "https://github.com/sponsors/ai"
                }
            ],
            "license": "MIT",
            "dependencies": {
                "nanoid": "^3.3.6",
                "picocolors": "^1.0.0",
                "source-map-js": "^1.0.2"
            },
            "engines": {
                "node": "^10 || ^12 || >=14"
            }
        },
        "node_modules/node-releases": {
            "version": "2.0.19",
            "resolved": "https://registry.npmjs.org/node-releases/-/node-releases-2.0.19.tgz",
            "integrity": "sha512-xxOWJsBKtzAq7DY0J+DTzuz58K8e7sJbdgwkbMWQe8UYB6ekmsQ45q0M/tJDsGaZmbC+l7n57UV8Hl5tHxO9uw==",
            "dev": true,
            "license": "MIT"
        },
        "node_modules/normalize-path": {
            "version": "3.0.0",
            "resolved": "https://registry.npmjs.org/normalize-path/-/normalize-path-3.0.0.tgz",
            "integrity": "sha512-6eZs5Ls3WtCisHWp9S2GUy8dqkpGi4BVSz3GaqiE6ezub0512ESztXUwUB6C6IKbQkY2Pnb/mD4WYojCRwcwLA==",
            "dev": true,
            "license": "MIT",
            "engines": {
                "node": ">=0.10.0"
            }
        },
        "node_modules/normalize-range": {
            "version": "0.1.2",
            "resolved": "https://registry.npmjs.org/normalize-range/-/normalize-range-0.1.2.tgz",
            "integrity": "sha512-bdok/XvKII3nUpklnV6P2hxtMNrCboOjAcyBuQnWEhO665FwrSNRxU+AqpsyvO6LgGYPspN+lu5CLtw4jPRKNA==",
            "dev": true,
            "license": "MIT",
            "engines": {
                "node": ">=0.10.0"
            }
        },
        "node_modules/object-assign": {
            "version": "4.1.1",
            "resolved": "https://registry.npmjs.org/object-assign/-/object-assign-4.1.1.tgz",
            "integrity": "sha512-rJgTQnkUnH1sFw8yT6VSU3zD3sWmu6sZhIseY8VX+GRu3P6F7Fu+JNDoXfklElbLJSnc3FUQHVe4cU5hj+BcUg==",
            "dev": true,
            "license": "MIT",
            "engines": {
                "node": ">=0.10.0"
            }
        },
        "node_modules/object-hash": {
            "version": "3.0.0",
            "resolved": "https://registry.npmjs.org/object-hash/-/object-hash-3.0.0.tgz",
            "integrity": "sha512-RSn9F68PjH9HqtltsSnqYC1XXoWe9Bju5+213R98cNGttag9q9yAOTzdbsqvIa7aNm5WffBZFpWYr2aWrklWAw==",
            "dev": true,
            "license": "MIT",
            "engines": {
                "node": ">= 6"
            }
        },
        "node_modules/package-json-from-dist": {
            "version": "1.0.1",
            "resolved": "https://registry.npmjs.org/package-json-from-dist/-/package-json-from-dist-1.0.1.tgz",
            "integrity": "sha512-UEZIS3/by4OC8vL3P2dTXRETpebLI2NiI5vIrjaD/5UtrkFX/tNbwjTSRAGC/+7CAo2pIcBaRgWmcBBHcsaCIw==",
            "dev": true,
            "license": "BlueOak-1.0.0"
        },
        "node_modules/path-key": {
            "version": "3.1.1",
            "resolved": "https://registry.npmjs.org/path-key/-/path-key-3.1.1.tgz",
            "integrity": "sha512-ojmeN0qd+y0jszEtoY48r0Peq5dwMEkIlCOu6Q5f41lfkswXuKtYrhgoTpLnyIcHm24Uhqx+5Tqm2InSwLhE6Q==",
            "dev": true,
            "license": "MIT",
            "engines": {
                "node": ">=8"
            }
        },
        "node_modules/path-parse": {
            "version": "1.0.7",
            "resolved": "https://registry.npmjs.org/path-parse/-/path-parse-1.0.7.tgz",
            "integrity": "sha512-LDJzPVEEEPR+y48z93A0Ed0yXb8pAByGWo/k5YYdYgpY2/2EsOsksJrq7lOHxryrVOn1ejG6oAp8ahvOIQD8sw==",
            "dev": true,
            "license": "MIT"
        },
        "node_modules/path-scurry": {
            "version": "1.11.1",
            "resolved": "https://registry.npmjs.org/path-scurry/-/path-scurry-1.11.1.tgz",
            "integrity": "sha512-Xa4Nw17FS9ApQFJ9umLiJS4orGjm7ZzwUrwamcGQuHSzDyth9boKDaycYdDcZDuqYATXw4HFXgaqWTctW/v1HA==",
            "dev": true,
            "license": "BlueOak-1.0.0",
            "dependencies": {
                "lru-cache": "^10.2.0",
                "minipass": "^5.0.0 || ^6.0.2 || ^7.0.0"
            },
            "engines": {
                "node": ">=16 || 14 >=14.18"
            },
            "funding": {
                "url": "https://github.com/sponsors/isaacs"
            }
        },
        "node_modules/picocolors": {
            "version": "1.1.1",
            "resolved": "https://registry.npmjs.org/picocolors/-/picocolors-1.1.1.tgz",
            "integrity": "sha512-xceH2snhtb5M9liqDsmEw56le376mTZkEX/jEb/RxNFyegNul7eNslCXP9FDj/Lcu0X8KEyMceP2ntpaHrDEVA==",
            "license": "ISC"
        },
        "node_modules/picomatch": {
            "version": "2.3.1",
            "resolved": "https://registry.npmjs.org/picomatch/-/picomatch-2.3.1.tgz",
            "integrity": "sha512-JU3teHTNjmE2VCGFzuY8EXzCDVwEqB2a8fsIvwaStHhAWJEeVd1o1QD80CU6+ZdEXXSLbSsuLwJjkCBWqRQUVA==",
            "dev": true,
            "license": "MIT",
            "engines": {
                "node": ">=8.6"
            },
            "funding": {
                "url": "https://github.com/sponsors/jonschlinkert"
            }
        },
        "node_modules/pify": {
            "version": "2.3.0",
            "resolved": "https://registry.npmjs.org/pify/-/pify-2.3.0.tgz",
            "integrity": "sha512-udgsAY+fTnvv7kI7aaxbqwWNb0AHiB0qBO89PZKPkoTmGOgdbrHDKD+0B2X4uTfJ/FT1R09r9gTsjUjNJotuog==",
            "dev": true,
            "license": "MIT",
            "engines": {
                "node": ">=0.10.0"
            }
        },
        "node_modules/pirates": {
            "version": "4.0.7",
            "resolved": "https://registry.npmjs.org/pirates/-/pirates-4.0.7.tgz",
            "integrity": "sha512-TfySrs/5nm8fQJDcBDuUng3VOUKsd7S+zqvbOTiGXHfxX4wK31ard+hoNuvkicM/2YFzlpDgABOevKSsB4G/FA==",
            "dev": true,
            "license": "MIT",
            "engines": {
                "node": ">= 6"
            }
        },
        "node_modules/postcss": {
            "version": "8.5.3",
            "resolved": "https://registry.npmjs.org/postcss/-/postcss-8.5.3.tgz",
            "integrity": "sha512-dle9A3yYxlBSrt8Fu+IpjGT8SY8hN0mlaA6GY8t0P5PjIOZemULz/E2Bnm/2dcUOena75OTNkHI76uZBNUUq3A==",
            "dev": true,
            "funding": [
                {
                    "type": "opencollective",
                    "url": "https://opencollective.com/postcss/"
                },
                {
                    "type": "tidelift",
                    "url": "https://tidelift.com/funding/github/npm/postcss"
                },
                {
                    "type": "github",
                    "url": "https://github.com/sponsors/ai"
                }
            ],
            "license": "MIT",
            "dependencies": {
                "nanoid": "^3.3.8",
                "picocolors": "^1.1.1",
                "source-map-js": "^1.2.1"
            },
            "engines": {
                "node": "^10 || ^12 || >=14"
            }
        },
        "node_modules/postcss-import": {
            "version": "15.1.0",
            "resolved": "https://registry.npmjs.org/postcss-import/-/postcss-import-15.1.0.tgz",
            "integrity": "sha512-hpr+J05B2FVYUAXHeK1YyI267J/dDDhMU6B6civm8hSY1jYJnBXxzKDKDswzJmtLHryrjhnDjqqp/49t8FALew==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "postcss-value-parser": "^4.0.0",
                "read-cache": "^1.0.0",
                "resolve": "^1.1.7"
            },
            "engines": {
                "node": ">=14.0.0"
            },
            "peerDependencies": {
                "postcss": "^8.0.0"
            }
        },
        "node_modules/postcss-js": {
            "version": "4.0.1",
            "resolved": "https://registry.npmjs.org/postcss-js/-/postcss-js-4.0.1.tgz",
            "integrity": "sha512-dDLF8pEO191hJMtlHFPRa8xsizHaM82MLfNkUHdUtVEV3tgTp5oj+8qbEqYM57SLfc74KSbw//4SeJma2LRVIw==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "camelcase-css": "^2.0.1"
            },
            "engines": {
                "node": "^12 || ^14 || >= 16"
            },
            "funding": {
                "type": "opencollective",
                "url": "https://opencollective.com/postcss/"
            },
            "peerDependencies": {
                "postcss": "^8.4.21"
            }
        },
        "node_modules/postcss-nested": {
            "version": "6.2.0",
            "resolved": "https://registry.npmjs.org/postcss-nested/-/postcss-nested-6.2.0.tgz",
            "integrity": "sha512-HQbt28KulC5AJzG+cZtj9kvKB93CFCdLvog1WFLf1D+xmMvPGlBstkpTEZfK5+AN9hfJocyBFCNiqyS48bpgzQ==",
            "dev": true,
            "funding": [
                {
                    "type": "opencollective",
                    "url": "https://opencollective.com/postcss/"
                },
                {
                    "type": "github",
                    "url": "https://github.com/sponsors/ai"
                }
            ],
            "license": "MIT",
            "dependencies": {
                "postcss-selector-parser": "^6.1.1"
            },
            "engines": {
                "node": ">=12.0"
            },
            "peerDependencies": {
                "postcss": "^8.2.14"
            }
        },
        "node_modules/postcss-selector-parser": {
            "version": "6.1.2",
            "resolved": "https://registry.npmjs.org/postcss-selector-parser/-/postcss-selector-parser-6.1.2.tgz",
            "integrity": "sha512-Q8qQfPiZ+THO/3ZrOrO0cJJKfpYCagtMUkXbnEfmgUjwXg6z/WBeOyS9APBBPCTSiDV+s4SwQGu8yFsiMRIudg==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "cssesc": "^3.0.0",
                "util-deprecate": "^1.0.2"
            },
            "engines": {
                "node": ">=4"
            }
        },
        "node_modules/postcss-value-parser": {
            "version": "4.2.0",
            "resolved": "https://registry.npmjs.org/postcss-value-parser/-/postcss-value-parser-4.2.0.tgz",
            "integrity": "sha512-1NNCs6uurfkVbeXG4S8JFT9t19m45ICnif8zWLd5oPSZ50QnwMfK+H3jv408d4jw/7Bttv5axS5IiHoLaVNHeQ==",
            "dev": true,
            "license": "MIT"
        },
        "node_modules/queue-microtask": {
            "version": "1.2.3",
            "resolved": "https://registry.npmjs.org/queue-microtask/-/queue-microtask-1.2.3.tgz",
            "integrity": "sha512-NuaNSa6flKT5JaSYQzJok04JzTL1CA6aGhv5rfLW3PgqA+M2ChpZQnAC8h8i4ZFkBS8X5RqkDBHA7r4hej3K9A==",
            "dev": true,
            "funding": [
                {
                    "type": "github",
                    "url": "https://github.com/sponsors/feross"
                },
                {
                    "type": "patreon",
                    "url": "https://www.patreon.com/feross"
                },
                {
                    "type": "consulting",
                    "url": "https://feross.org/support"
                }
            ],
            "license": "MIT"
        },
        "node_modules/react": {
            "version": "18.3.1",
            "resolved": "https://registry.npmjs.org/react/-/react-18.3.1.tgz",
            "integrity": "sha512-wS+hAgJShR0KhEvPJArfuPVN1+Hz1t0Y6n5jLrGQbkb4urgPE/0Rve+1kMB1v/oWgHgm4WIcV+i7F2pTVj+2iQ==",
            "license": "MIT",
            "dependencies": {
                "loose-envify": "^1.1.0"
            },
            "engines": {
                "node": ">=0.10.0"
            }
        },
        "node_modules/react-dom": {
            "version": "18.3.1",
            "resolved": "https://registry.npmjs.org/react-dom/-/react-dom-18.3.1.tgz",
            "integrity": "sha512-5m4nQKp+rZRb09LNH59GM4BxTh9251/ylbKIbpe7TpGxfJ+9kv6BLkLBXIjjspbgbnIBNqlI23tRnTWT0snUIw==",
            "license": "MIT",
            "dependencies": {
                "loose-envify": "^1.1.0",
                "scheduler": "^0.23.2"
            },
            "peerDependencies": {
                "react": "^18.3.1"
            }
        },
        "node_modules/read-cache": {
            "version": "1.0.0",
            "resolved": "https://registry.npmjs.org/read-cache/-/read-cache-1.0.0.tgz",
            "integrity": "sha512-Owdv/Ft7IjOgm/i0xvNDZ1LrRANRfew4b2prF3OWMQLxLfu3bS8FVhCsrSCMK4lR56Y9ya+AThoTpDCTxCmpRA==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "pify": "^2.3.0"
            }
        },
        "node_modules/readdirp": {
            "version": "3.6.0",
            "resolved": "https://registry.npmjs.org/readdirp/-/readdirp-3.6.0.tgz",
            "integrity": "sha512-hOS089on8RduqdbhvQ5Z37A0ESjsqz6qnRcffsMU3495FuTdqSm+7bhJ29JvIOsBDEEnan5DPu9t3To9VRlMzA==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "picomatch": "^2.2.1"
            },
            "engines": {
                "node": ">=8.10.0"
            }
        },
        "node_modules/resolve": {
            "version": "1.22.10",
            "resolved": "https://registry.npmjs.org/resolve/-/resolve-1.22.10.tgz",
            "integrity": "sha512-NPRy+/ncIMeDlTAsuqwKIiferiawhefFJtkNSW0qZJEqMEb+qBt/77B/jGeeek+F0uOeN05CDa6HXbbIgtVX4w==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "is-core-module": "^2.16.0",
                "path-parse": "^1.0.7",
                "supports-preserve-symlinks-flag": "^1.0.0"
            },
            "bin": {
                "resolve": "bin/resolve"
            },
            "engines": {
                "node": ">= 0.4"
            },
            "funding": {
                "url": "https://github.com/sponsors/ljharb"
            }
        },
        "node_modules/reusify": {
            "version": "1.1.0",
            "resolved": "https://registry.npmjs.org/reusify/-/reusify-1.1.0.tgz",
            "integrity": "sha512-g6QUff04oZpHs0eG5p83rFLhHeV00ug/Yf9nZM6fLeUrPguBTkTQOdpAWWspMh55TZfVQDPaN3NQJfbVRAxdIw==",
            "dev": true,
            "license": "MIT",
            "engines": {
                "iojs": ">=1.0.0",
                "node": ">=0.10.0"
            }
        },
        "node_modules/run-parallel": {
            "version": "1.2.0",
            "resolved": "https://registry.npmjs.org/run-parallel/-/run-parallel-1.2.0.tgz",
            "integrity": "sha512-5l4VyZR86LZ/lDxZTR6jqL8AFE2S0IFLMP26AbjsLVADxHdhB/c0GUsH+y39UfCi3dzz8OlQuPmnaJOMoDHQBA==",
            "dev": true,
            "funding": [
                {
                    "type": "github",
                    "url": "https://github.com/sponsors/feross"
                },
                {
                    "type": "patreon",
                    "url": "https://www.patreon.com/feross"
                },
                {
                    "type": "consulting",
                    "url": "https://feross.org/support"
                }
            ],
            "license": "MIT",
            "dependencies": {
                "queue-microtask": "^1.2.2"
            }
        },
        "node_modules/scheduler": {
            "version": "0.23.2",
            "resolved": "https://registry.npmjs.org/scheduler/-/scheduler-0.23.2.tgz",
            "integrity": "sha512-UOShsPwz7NrMUqhR6t0hWjFduvOzbtv7toDH1/hIrfRNIDBnnBWd0CwJTGvTpngVlmwGCdP9/Zl/tVrDqcuYzQ==",
            "license": "MIT",
            "dependencies": {
                "loose-envify": "^1.1.0"
            }
        },
        "node_modules/shebang-command": {
            "version": "2.0.0",
            "resolved": "https://registry.npmjs.org/shebang-command/-/shebang-command-2.0.0.tgz",
            "integrity": "sha512-kHxr2zZpYtdmrN1qDjrrX/Z1rR1kG8Dx+gkpK1G4eXmvXswmcE1hTWBWYUzlraYw1/yZp6YuDY77YtvbN0dmDA==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "shebang-regex": "^3.0.0"
            },
            "engines": {
                "node": ">=8"
            }
        },
        "node_modules/shebang-regex": {
            "version": "3.0.0",
            "resolved": "https://registry.npmjs.org/shebang-regex/-/shebang-regex-3.0.0.tgz",
            "integrity": "sha512-7++dFhtcx3353uBaq8DDR4NuxBetBzC7ZQOhmTQInHEd6bSrXdiEyzCvG07Z44UYdLShWUyXt5M/yhz8ekcb1A==",
            "dev": true,
            "license": "MIT",
            "engines": {
                "node": ">=8"
            }
        },
        "node_modules/signal-exit": {
            "version": "4.1.0",
            "resolved": "https://registry.npmjs.org/signal-exit/-/signal-exit-4.1.0.tgz",
            "integrity": "sha512-bzyZ1e88w9O1iNJbKnOlvYTrWPDl46O1bG0D3XInv+9tkPrxrN8jUUTiFlDkkmKWgn1M6CfIA13SuGqOa9Korw==",
            "dev": true,
            "license": "ISC",
            "engines": {
                "node": ">=14"
            },
            "funding": {
                "url": "https://github.com/sponsors/isaacs"
            }
        },
        "node_modules/source-map-js": {
            "version": "1.2.1",
            "resolved": "https://registry.npmjs.org/source-map-js/-/source-map-js-1.2.1.tgz",
            "integrity": "sha512-UXWMKhLOwVKb728IUtQPXxfYU+usdybtUrK/8uGE8CQMvrhOpwvzDBwj0QhSL7MQc7vIsISBG8VQ8+IDQxpfQA==",
            "license": "BSD-3-Clause",
            "engines": {
                "node": ">=0.10.0"
            }
        },
        "node_modules/streamsearch": {
            "version": "1.1.0",
            "resolved": "https://registry.npmjs.org/streamsearch/-/streamsearch-1.1.0.tgz",
            "integrity": "sha512-Mcc5wHehp9aXz1ax6bZUyY5afg9u2rv5cqQI3mRrYkGC8rW2hM02jWuwjtL++LS5qinSyhj2QfLyNsuc+VsExg==",
            "engines": {
                "node": ">=10.0.0"
            }
        },
        "node_modules/string-width": {
            "version": "5.1.2",
            "resolved": "https://registry.npmjs.org/string-width/-/string-width-5.1.2.tgz",
            "integrity": "sha512-HnLOCR3vjcY8beoNLtcjZ5/nxn2afmME6lhrDrebokqMap+XbeW8n9TXpPDOqdGK5qcI3oT0GKTW6wC7EMiVqA==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "eastasianwidth": "^0.2.0",
                "emoji-regex": "^9.2.2",
                "strip-ansi": "^7.0.1"
            },
            "engines": {
                "node": ">=12"
            },
            "funding": {
                "url": "https://github.com/sponsors/sindresorhus"
            }
        },
        "node_modules/string-width-cjs": {
            "name": "string-width",
            "version": "4.2.3",
            "resolved": "https://registry.npmjs.org/string-width/-/string-width-4.2.3.tgz",
            "integrity": "sha512-wKyQRQpjJ0sIp62ErSZdGsjMJWsap5oRNihHhu6G7JVO/9jIB6UyevL+tXuOqrng8j/cxKTWyWUwvSTriiZz/g==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "emoji-regex": "^8.0.0",
                "is-fullwidth-code-point": "^3.0.0",
                "strip-ansi": "^6.0.1"
            },
            "engines": {
                "node": ">=8"
            }
        },
        "node_modules/string-width-cjs/node_modules/ansi-regex": {
            "version": "5.0.1",
            "resolved": "https://registry.npmjs.org/ansi-regex/-/ansi-regex-5.0.1.tgz",
            "integrity": "sha512-quJQXlTSUGL2LH9SUXo8VwsY4soanhgo6LNSm84E1LBcE8s3O0wpdiRzyR9z/ZZJMlMWv37qOOb9pdJlMUEKFQ==",
            "dev": true,
            "license": "MIT",
            "engines": {
                "node": ">=8"
            }
        },
        "node_modules/string-width-cjs/node_modules/emoji-regex": {
            "version": "8.0.0",
            "resolved": "https://registry.npmjs.org/emoji-regex/-/emoji-regex-8.0.0.tgz",
            "integrity": "sha512-MSjYzcWNOA0ewAHpz0MxpYFvwg6yjy1NG3xteoqz644VCo/RPgnr1/GGt+ic3iJTzQ8Eu3TdM14SawnVUmGE6A==",
            "dev": true,
            "license": "MIT"
        },
        "node_modules/string-width-cjs/node_modules/strip-ansi": {
            "version": "6.0.1",
            "resolved": "https://registry.npmjs.org/strip-ansi/-/strip-ansi-6.0.1.tgz",
            "integrity": "sha512-Y38VPSHcqkFrCpFnQ9vuSXmquuv5oXOKpGeT6aGrr3o3Gc9AlVa6JBfUSOCnbxGGZF+/0ooI7KrPuUSztUdU5A==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "ansi-regex": "^5.0.1"
            },
            "engines": {
                "node": ">=8"
            }
        },
        "node_modules/strip-ansi": {
            "version": "7.1.0",
            "resolved": "https://registry.npmjs.org/strip-ansi/-/strip-ansi-7.1.0.tgz",
            "integrity": "sha512-iq6eVVI64nQQTRYq2KtEg2d2uU7LElhTJwsH4YzIHZshxlgZms/wIc4VoDQTlG/IvVIrBKG06CrZnp0qv7hkcQ==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "ansi-regex": "^6.0.1"
            },
            "engines": {
                "node": ">=12"
            },
            "funding": {
                "url": "https://github.com/chalk/strip-ansi?sponsor=1"
            }
        },
        "node_modules/strip-ansi-cjs": {
            "name": "strip-ansi",
            "version": "6.0.1",
            "resolved": "https://registry.npmjs.org/strip-ansi/-/strip-ansi-6.0.1.tgz",
            "integrity": "sha512-Y38VPSHcqkFrCpFnQ9vuSXmquuv5oXOKpGeT6aGrr3o3Gc9AlVa6JBfUSOCnbxGGZF+/0ooI7KrPuUSztUdU5A==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "ansi-regex": "^5.0.1"
            },
            "engines": {
                "node": ">=8"
            }
        },
        "node_modules/strip-ansi-cjs/node_modules/ansi-regex": {
            "version": "5.0.1",
            "resolved": "https://registry.npmjs.org/ansi-regex/-/ansi-regex-5.0.1.tgz",
            "integrity": "sha512-quJQXlTSUGL2LH9SUXo8VwsY4soanhgo6LNSm84E1LBcE8s3O0wpdiRzyR9z/ZZJMlMWv37qOOb9pdJlMUEKFQ==",
            "dev": true,
            "license": "MIT",
            "engines": {
                "node": ">=8"
            }
        },
        "node_modules/styled-jsx": {
            "version": "5.1.1",
            "resolved": "https://registry.npmjs.org/styled-jsx/-/styled-jsx-5.1.1.tgz",
            "integrity": "sha512-pW7uC1l4mBZ8ugbiZrcIsiIvVx1UmTfw7UkC3Um2tmfUq9Bhk8IiyEIPl6F8agHgjzku6j0xQEZbfA5uSgSaCw==",
            "license": "MIT",
            "dependencies": {
                "client-only": "0.0.1"
            },
            "engines": {
                "node": ">= 12.0.0"
            },
            "peerDependencies": {
                "react": ">= 16.8.0 || 17.x.x || ^18.0.0-0"
            },
            "peerDependenciesMeta": {
                "@babel/core": {
                    "optional": true
                },
                "babel-plugin-macros": {
                    "optional": true
                }
            }
        },
        "node_modules/sucrase": {
            "version": "3.35.0",
            "resolved": "https://registry.npmjs.org/sucrase/-/sucrase-3.35.0.tgz",
            "integrity": "sha512-8EbVDiu9iN/nESwxeSxDKe0dunta1GOlHufmSSXxMD2z2/tMZpDMpvXQGsc+ajGo8y2uYUmixaSRUc/QPoQ0GA==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "@jridgewell/gen-mapping": "^0.3.2",
                "commander": "^4.0.0",
                "glob": "^10.3.10",
                "lines-and-columns": "^1.1.6",
                "mz": "^2.7.0",
                "pirates": "^4.0.1",
                "ts-interface-checker": "^0.1.9"
            },
            "bin": {
                "sucrase": "bin/sucrase",
                "sucrase-node": "bin/sucrase-node"
            },
            "engines": {
                "node": ">=16 || 14 >=14.17"
            }
        },
        "node_modules/supports-preserve-symlinks-flag": {
            "version": "1.0.0",
            "resolved": "https://registry.npmjs.org/supports-preserve-symlinks-flag/-/supports-preserve-symlinks-flag-1.0.0.tgz",
            "integrity": "sha512-ot0WnXS9fgdkgIcePe6RHNk1WA8+muPa6cSjeR3V8K27q9BB1rTE3R1p7Hv0z1ZyAc8s6Vvv8DIyWf681MAt0w==",
            "dev": true,
            "license": "MIT",
            "engines": {
                "node": ">= 0.4"
            },
            "funding": {
                "url": "https://github.com/sponsors/ljharb"
            }
        },
        "node_modules/tailwindcss": {
            "version": "3.4.17",
            "resolved": "https://registry.npmjs.org/tailwindcss/-/tailwindcss-3.4.17.tgz",
            "integrity": "sha512-w33E2aCvSDP0tW9RZuNXadXlkHXqFzSkQew/aIa2i/Sj8fThxwovwlXHSPXTbAHwEIhBFXAedUhP2tueAKP8Og==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "@alloc/quick-lru": "^5.2.0",
                "arg": "^5.0.2",
                "chokidar": "^3.6.0",
                "didyoumean": "^1.2.2",
                "dlv": "^1.1.3",
                "fast-glob": "^3.3.2",
                "glob-parent": "^6.0.2",
                "is-glob": "^4.0.3",
                "jiti": "^1.21.6",
                "lilconfig": "^3.1.3",
                "micromatch": "^4.0.8",
                "normalize-path": "^3.0.0",
                "object-hash": "^3.0.0",
                "picocolors": "^1.1.1",
                "postcss": "^8.4.47",
                "postcss-import": "^15.1.0",
                "postcss-js": "^4.0.1",
                "postcss-load-config": "^4.0.2",
                "postcss-nested": "^6.2.0",
                "postcss-selector-parser": "^6.1.2",
                "resolve": "^1.22.8",
                "sucrase": "^3.35.0"
            },
            "bin": {
                "tailwind": "lib/cli.js",
                "tailwindcss": "lib/cli.js"
            },
            "engines": {
                "node": ">=14.0.0"
            }
        },
        "node_modules/tailwindcss/node_modules/postcss-load-config": {
            "version": "4.0.2",
            "resolved": "https://registry.npmjs.org/postcss-load-config/-/postcss-load-config-4.0.2.tgz",
            "integrity": "sha512-bSVhyJGL00wMVoPUzAVAnbEoWyqRxkjv64tUl427SKnPrENtq6hJwUojroMz2VB+Q1edmi4IfrAPpami5VVgMQ==",
            "dev": true,
            "funding": [
                {
                    "type": "opencollective",
                    "url": "https://opencollective.com/postcss/"
                },
                {
                    "type": "github",
                    "url": "https://github.com/sponsors/ai"
                }
            ],
            "license": "MIT",
            "dependencies": {
                "lilconfig": "^3.0.0",
                "yaml": "^2.3.4"
            },
            "engines": {
                "node": ">= 14"
            },
            "peerDependencies": {
                "postcss": ">=8.0.9",
                "ts-node": ">=9.0.0"
            },
            "peerDependenciesMeta": {
                "postcss": {
                    "optional": true
                },
                "ts-node": {
                    "optional": true
                }
            }
        },
        "node_modules/thenify": {
            "version": "3.3.1",
            "resolved": "https://registry.npmjs.org/thenify/-/thenify-3.3.1.tgz",
            "integrity": "sha512-RVZSIV5IG10Hk3enotrhvz0T9em6cyHBLkH/YAZuKqd8hRkKhSfCGIcP2KUY0EPxndzANBmNllzWPwak+bheSw==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "any-promise": "^1.0.0"
            }
        },
        "node_modules/thenify-all": {
            "version": "1.6.0",
            "resolved": "https://registry.npmjs.org/thenify-all/-/thenify-all-1.6.0.tgz",
            "integrity": "sha512-RNxQH/qI8/t3thXJDwcstUO4zeqo64+Uy/+sNVRBx4Xn2OX+OZ9oP+iJnNFqplFra2ZUVeKCSa2oVWi3T4uVmA==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "thenify": ">= 3.1.0 < 4"
            },
            "engines": {
                "node": ">=0.8"
            }
        },
        "node_modules/to-regex-range": {
            "version": "5.0.1",
            "resolved": "https://registry.npmjs.org/to-regex-range/-/to-regex-range-5.0.1.tgz",
            "integrity": "sha512-65P7iz6X5yEr1cwcgvQxbbIw7Uk3gOy5dIdtZ4rDveLqhrdJP+Li/Hx6tyK0NEb+2GCyneCMJiGqrADCSNk8sQ==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "is-number": "^7.0.0"
            },
            "engines": {
                "node": ">=8.0"
            }
        },
        "node_modules/ts-interface-checker": {
            "version": "0.1.13",
            "resolved": "https://registry.npmjs.org/ts-interface-checker/-/ts-interface-checker-0.1.13.tgz",
            "integrity": "sha512-Y/arvbn+rrz3JCKl9C4kVNfTfSm2/mEp5FSz5EsZSANGPSlQrpRI5M4PKF+mJnE52jOO90PnPSc3Ur3bTQw0gA==",
            "dev": true,
            "license": "Apache-2.0"
        },
        "node_modules/tslib": {
            "version": "2.8.1",
            "resolved": "https://registry.npmjs.org/tslib/-/tslib-2.8.1.tgz",
            "integrity": "sha512-oJFu94HQb+KVduSUQL7wnpmqnfmLsOA/nAh6b6EH0wCEoK0/mPeXU6c3wKDV83MkOuHPRHtSXKKU99IBazS/2w==",
            "license": "0BSD"
        },
        "node_modules/typescript": {
            "version": "5.8.3",
            "resolved": "https://registry.npmjs.org/typescript/-/typescript-5.8.3.tgz",
            "integrity": "sha512-p1diW6TqL9L07nNxvRMM7hMMw4c5XOo/1ibL4aAIGmSAt9slTE1Xgw5KWuof2uTOvCg9BY7ZRi+GaF+7sfgPeQ==",
            "dev": true,
            "license": "Apache-2.0",
            "bin": {
                "tsc": "bin/tsc",
                "tsserver": "bin/tsserver"
            },
            "engines": {
                "node": ">=14.17"
            }
        },
        "node_modules/undici-types": {
            "version": "6.21.0",
            "resolved": "https://registry.npmjs.org/undici-types/-/undici-types-6.21.0.tgz",
            "integrity": "sha512-iwDZqg0QAGrg9Rav5H4n0M64c3mkR59cJ6wQp+7C4nI0gsmExaedaYLNO44eT4AtBBwjbTiGPMlt2Md0T9H9JQ==",
            "dev": true,
            "license": "MIT"
        },
        "node_modules/update-browserslist-db": {
            "version": "1.1.3",
            "resolved": "https://registry.npmjs.org/update-browserslist-db/-/update-browserslist-db-1.1.3.tgz",
            "integrity": "sha512-UxhIZQ+QInVdunkDAaiazvvT/+fXL5Osr0JZlJulepYu6Jd7qJtDZjlur0emRlT71EN3ScPoE7gvsuIKKNavKw==",
            "dev": true,
            "funding": [
                {
                    "type": "opencollective",
                    "url": "https://opencollective.com/browserslist"
                },
                {
                    "type": "tidelift",
                    "url": "https://tidelift.com/funding/github/npm/browserslist"
                },
                {
                    "type": "github",
                    "url": "https://github.com/sponsors/ai"
                }
            ],
            "license": "MIT",
            "dependencies": {
                "escalade": "^3.2.0",
                "picocolors": "^1.1.1"
            },
            "bin": {
                "update-browserslist-db": "cli.js"
            },
            "peerDependencies": {
                "browserslist": ">= 4.21.0"
            }
        },
        "node_modules/util-deprecate": {
            "version": "1.0.2",
            "resolved": "https://registry.npmjs.org/util-deprecate/-/util-deprecate-1.0.2.tgz",
            "integrity": "sha512-EPD5q1uXyFxJpCrLnCc1nHnq3gOa6DZBocAIiI2TaSCA7VCJ1UJDMagCzIkXNsUYfD1daK//LTEQ8xiIbrHtcw==",
            "dev": true,
            "license": "MIT"
        },
        "node_modules/which": {
            "version": "2.0.2",
            "resolved": "https://registry.npmjs.org/which/-/which-2.0.2.tgz",
            "integrity": "sha512-BLI3Tl1TW3Pvl70l3yq3Y64i+awpwXqsGBYWkkqMtnbXgrMD+yj7rhW0kuEDxzJaYXGjEW5ogapKNMEKNMjibA==",
            "dev": true,
            "license": "ISC",
            "dependencies": {
                "isexe": "^2.0.0"
            },
            "bin": {
                "node-which": "bin/node-which"
            },
            "engines": {
                "node": ">= 8"
            }
        },
        "node_modules/wrap-ansi": {
            "version": "8.1.0",
            "resolved": "https://registry.npmjs.org/wrap-ansi/-/wrap-ansi-8.1.0.tgz",
            "integrity": "sha512-si7QWI6zUMq56bESFvagtmzMdGOtoxfR+Sez11Mobfc7tm+VkUckk9bW2UeffTGVUbOksxmSw0AA2gs8g71NCQ==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "ansi-styles": "^6.1.0",
                "string-width": "^5.0.1",
                "strip-ansi": "^7.0.1"
            },
            "engines": {
                "node": ">=12"
            },
            "funding": {
                "url": "https://github.com/chalk/wrap-ansi?sponsor=1"
            }
        },
        "node_modules/wrap-ansi-cjs": {
            "name": "wrap-ansi",
            "version": "7.0.0",
            "resolved": "https://registry.npmjs.org/wrap-ansi/-/wrap-ansi-7.0.0.tgz",
            "integrity": "sha512-YVGIj2kamLSTxw6NsZjoBxfSwsn0ycdesmc4p+Q21c5zPuZ1pl+NfxVdxPtdHvmNVOQ6XSYG4AUtyt/Fi7D16Q==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "ansi-styles": "^4.0.0",
                "string-width": "^4.1.0",
                "strip-ansi": "^6.0.0"
            },
            "engines": {
                "node": ">=10"
            },
            "funding": {
                "url": "https://github.com/chalk/wrap-ansi?sponsor=1"
            }
        },
        "node_modules/wrap-ansi-cjs/node_modules/ansi-regex": {
            "version": "5.0.1",
            "resolved": "https://registry.npmjs.org/ansi-regex/-/ansi-regex-5.0.1.tgz",
            "integrity": "sha512-quJQXlTSUGL2LH9SUXo8VwsY4soanhgo6LNSm84E1LBcE8s3O0wpdiRzyR9z/ZZJMlMWv37qOOb9pdJlMUEKFQ==",
            "dev": true,
            "license": "MIT",
            "engines": {
                "node": ">=8"
            }
        },
        "node_modules/wrap-ansi-cjs/node_modules/ansi-styles": {
            "version": "4.3.0",
            "resolved": "https://registry.npmjs.org/ansi-styles/-/ansi-styles-4.3.0.tgz",
            "integrity": "sha512-zbB9rCJAT1rbjiVDb2hqKFHNYLxgtk8NURxZ3IZwD3F6NtxbXZQCnnSi1Lkx+IDohdPlFp222wVALIheZJQSEg==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "color-convert": "^2.0.1"
            },
            "engines": {
                "node": ">=8"
            },
            "funding": {
                "url": "https://github.com/chalk/ansi-styles?sponsor=1"
            }
        },
        "node_modules/wrap-ansi-cjs/node_modules/emoji-regex": {
            "version": "8.0.0",
            "resolved": "https://registry.npmjs.org/emoji-regex/-/emoji-regex-8.0.0.tgz",
            "integrity": "sha512-MSjYzcWNOA0ewAHpz0MxpYFvwg6yjy1NG3xteoqz644VCo/RPgnr1/GGt+ic3iJTzQ8Eu3TdM14SawnVUmGE6A==",
            "dev": true,
            "license": "MIT"
        },
        "node_modules/wrap-ansi-cjs/node_modules/string-width": {
            "version": "4.2.3",
            "resolved": "https://registry.npmjs.org/string-width/-/string-width-4.2.3.tgz",
            "integrity": "sha512-wKyQRQpjJ0sIp62ErSZdGsjMJWsap5oRNihHhu6G7JVO/9jIB6UyevL+tXuOqrng8j/cxKTWyWUwvSTriiZz/g==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "emoji-regex": "^8.0.0",
                "is-fullwidth-code-point": "^3.0.0",
                "strip-ansi": "^6.0.1"
            },
            "engines": {
                "node": ">=8"
            }
        },
        "node_modules/wrap-ansi-cjs/node_modules/strip-ansi": {
            "version": "6.0.1",
            "resolved": "https://registry.npmjs.org/strip-ansi/-/strip-ansi-6.0.1.tgz",
            "integrity": "sha512-Y38VPSHcqkFrCpFnQ9vuSXmquuv5oXOKpGeT6aGrr3o3Gc9AlVa6JBfUSOCnbxGGZF+/0ooI7KrPuUSztUdU5A==",
            "dev": true,
            "license": "MIT",
            "dependencies": {
                "ansi-regex": "^5.0.1"
            },
            "engines": {
                "node": ">=8"
            }
        },
        "node_modules/yaml": {
            "version": "2.7.1",
            "resolved": "https://registry.npmjs.org/yaml/-/yaml-2.7.1.tgz",
            "integrity": "sha512-10ULxpnOCQXxJvBgxsn9ptjq6uviG/htZKk9veJGhlqn3w/DxQ631zFF+nlQXLwmImeS5amR2dl2U8sg6U9jsQ==",
            "dev": true,
            "license": "ISC",
            "bin": {
                "yaml": "bin.mjs"
            },
            "engines": {
                "node": ">= 14"
            }
        }
    }
}

```

## 📄 `frontend\package.json`

```json
{
    "name": "bookverse-frontend",
    "version": "1.0.0",
    "scripts": {
        "dev": "next dev",
        "build": "next build",
        "start": "next start -p $PORT"
    },
    "dependencies": {
        "next": "14.1.0",
        "react": "^18.2.0",
        "react-dom": "^18.2.0"
    },
    "devDependencies": {
        "@types/node": "22.15.14",
        "@types/react": "19.1.3",
        "autoprefixer": "^10.4.13",
        "postcss": "^8.4.21",
        "tailwindcss": "^3.3.2",
        "typescript": "^5.0.0"
    }
}

```

## 📄 `frontend\postcss.config.js`

```javascript
module.exports = {
    plugins: {
      tailwindcss: {},
      autoprefixer: {},
    },
  };
  
```

## 📄 `frontend\setup.py`

```python
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

```

## 📄 `frontend\tailwind.config.ts`

```typescript
module.exports = { darkMode: 'class', content: ['./app/**/*.{ts,tsx}'], theme: { extend: {} }, plugins: [] };
```

## 📄 `frontend\tsconfig.json`

```json
{
  "compilerOptions": {
    "target": "esnext",
    "module": "esnext",
    "jsx": "preserve",
    "strict": true,
    "lib": [
      "dom",
      "dom.iterable",
      "esnext"
    ],
    "allowJs": true,
    "skipLibCheck": true,
    "noEmit": true,
    "incremental": true,
    "esModuleInterop": true,
    "moduleResolution": "node",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "plugins": [
      {
        "name": "next"
      }
    ]
  },
  "include": [
    "next-env.d.ts",
    ".next/types/**/*.ts",
    "**/*.ts",
    "**/*.tsx"
  ],
  "exclude": [
    "node_modules"
  ]
}

```

## 📄 `frontend\app\layout.tsx`

```
export default function Layout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>
        <header style={{ padding: '1rem', backgroundColor: '#f5f5f5', fontWeight: 'bold' }}>
          Bookverse
        </header>
        <main style={{ padding: '1rem' }}>{children}</main>
      </body>
    </html>
  );
}
```

## 📄 `frontend\app\page.tsx`

```
export default function Home() {
  return (
    <div style={{ textAlign: 'center', marginTop: '10%' }}>
      <h1 style={{ fontSize: '2rem', fontWeight: 'bold' }}>Welcome to Bookverse 📚</h1>
      <p style={{ marginTop: '1rem' }}>당신의 독서 모임, 지금 시작하세요.</p>
    </div>
  );
}
```

## 📄 `frontend\app\books\page.tsx`

```
export default function Books() {
  return <div>도서 탐색</div>;
}
```

## 📄 `frontend\app\groups\[groupId]\page.tsx`

```
export default function GroupDashboard() {
  return <div>그룹 대시보드</div>;
}
```

## 📄 `frontend\app\groups\[groupId]\me\page.tsx`

```
export default function GroupMyPage() {
  return <div>그룹 내 마이페이지</div>;
}
```

## 📄 `frontend\app\groups\[groupId]\posts\[postId]\page.tsx`

```
export default function GroupPostDetail() {
  return <div>그룹 글 상세</div>;
}
```

## 📄 `frontend\app\groups\[groupId]\write\page.tsx`

```
export default function GroupWrite() {
  return <div>그룹 글쓰기</div>;
}
```

## 📄 `frontend\app\login\page.tsx`

```
export default function Login() {
  return <div>로그인</div>;
}
```

## 📄 `frontend\app\my\page.tsx`

```
export default function MyPage() {
  return <div>전역 마이페이지</div>;
}
```

## 📄 `frontend\app\posts\[postId]\page.tsx`

```
export default function PersonalPostDetail() {
  return <div>개인 글 상세</div>;
}
```

## 📄 `frontend\app\signup\page.tsx`

```
export default function Signup() {
  return <div>회원가입</div>;
}
```

## 📄 `frontend\app\write\page.tsx`

```
export default function PersonalWrite() {
  return <div>개인 글쓰기</div>;
}
```

## 📄 `frontend\lib\api.ts`

```typescript
const API_URL = process.env.NEXT_PUBLIC_API_URL;

export async function fetchPosts() {
  const res = await fetch(`${API_URL}/api/v1/posts`);
  if (!res.ok) {
    throw new Error("Failed to fetch posts");
  }
  return res.json();
}

```

## 📄 `frontend\lib\auth.ts`

```typescript
// 인증 유틸
```

## 📄 `frontend\lib\utils.ts`

```typescript
// 공통 유틸
```

## 📄 `frontend\styles\globals.css`

```css
/* Tailwind base 설정 */
@tailwind base;
@tailwind components;
@tailwind utilities;
```

