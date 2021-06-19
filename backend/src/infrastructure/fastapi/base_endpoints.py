from fastapi import APIRouter


router = APIRouter()


@router.get("/ping")
def ping() -> str:
    return "pong"
