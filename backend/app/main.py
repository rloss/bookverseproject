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