from fastapi import FastAPI, APIRouter

app = FastAPI()

router = APIRouter()

@router.get("/hello")
def say_hello():
    return {"message": "hi"}

app.include_router(router)
