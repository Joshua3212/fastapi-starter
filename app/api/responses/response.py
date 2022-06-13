import json
from typing import Union

from core.config import Settings
from starlette.background import BackgroundTask
from starlette.responses import Response


class JsonResponse(Response):
    media_type = "application/json"

    def __init__(
            self,
            content: Union[dict, list],
            status_code: int = 200,
            headers=None,
            background: BackgroundTask = None,
    ) -> None:
        if headers is None:
            headers = {}
        if type(content) == list:
            content = {"items": content, "length": len(content)}
        self.body = json.dumps(content).encode(self.charset)
        self.status_code = status_code
        self.init_headers({**Settings().assemble_headers(), **headers})
        self.background = background
