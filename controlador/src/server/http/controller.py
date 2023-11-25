from aiohttp.web import View
from abc import ABC

from .responses import ResponseNotFound, AbstractResponse


class Controller(View, ABC):
    async def get(self) -> AbstractResponse:
        return ResponseNotFound()

    async def post(self) -> AbstractResponse:
        return ResponseNotFound()

    async def put(self) -> AbstractResponse:
        return ResponseNotFound()

    async def delete(self) -> AbstractResponse:
        return ResponseNotFound()

    async def patch(self) -> AbstractResponse:
        return ResponseNotFound()
