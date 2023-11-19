from aiohttp.web import View
from abc import ABC

from .responses import ResponseNotFound, Response


class Controller(View, ABC):
    async def get(self) -> Response:
        return ResponseNotFound()

    async def post(self) -> Response:
        return ResponseNotFound()

    async def put(self) -> Response:
        return ResponseNotFound()

    async def delete(self) -> Response:
        return ResponseNotFound()

    async def patch(self) -> Response:
        return ResponseNotFound()
