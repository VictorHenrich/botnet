from aiohttp.web import View
from abc import ABC

from .responses import ResponseNotFound


class Controller(View, ABC):
    async def get(self):
        return ResponseNotFound()

    async def post(self):
        return ResponseNotFound()

    async def put(self):
        return ResponseNotFound()

    async def delete(self):
        return ResponseNotFound()

    async def patch(self):
        return ResponseNotFound()