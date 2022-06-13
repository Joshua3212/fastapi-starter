import json

from core.config import Settings
from starlette.background import BackgroundTask
from starlette.responses import Response


class ErrorResponse(Response):
    media_type = "application/json"

    def __init__(
            self,
            error: str = None,
            error_details: str = None,
            error_code: str = None,
            status_code: int = 500,
            headers=None,
            background: BackgroundTask = None,
    ) -> None:
        if headers is None:
            headers = {}
        self.body = json.dumps(
            {
                "error": error,
                "errorCode": error_code,
                "errorDetails": error_details,
            }
        ).encode(self.charset)
        self.status_code = status_code
        self.init_headers({**Settings().assemble_headers(), **headers})
        self.background = background
