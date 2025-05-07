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
