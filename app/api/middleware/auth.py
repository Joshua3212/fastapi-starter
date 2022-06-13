from typing import Tuple

from fastapi import Request
from responses.error_response import ErrorResponse


def auth_middleware(request: Request) -> Tuple[ErrorResponse, str]:
    try:
        token = request.headers.get("Authorization").split("Token ")[1]
    except:
        token = None
    if not token:
        return ErrorResponse(
            "No valid Authorization Token found.",
            "Check if your Authorization Token is valid.",
            "invalidAuthTokenException",
            401,
        )
    return token
