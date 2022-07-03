from api.endpoints.example import router as example_router
from core.config import Settings
from fastapi import APIRouter

api_router = APIRouter()

api_router.include_router(example_router,
                          prefix=Settings().API_PREFIX)  # here we get the prefix from the config.json file
