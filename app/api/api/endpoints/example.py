from fastapi import APIRouter

router = APIRouter()


@router.get("/ping")
async def hello_world():
    return {
        "message": "Hello World",
    }
