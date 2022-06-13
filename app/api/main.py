from fastapi import FastAPI, Request

from api.api import api_router
from middleware.auth import auth_middleware
from responses.exceptions import exceptions

app = FastAPI(exception_handlers=exceptions)


@app.middleware("http")
async def check_auth_token(request: Request, call_next):
    auth_middleware(request)  # an example middleware; feel free to remove it
    return await call_next(request)


app.include_router(api_router)
