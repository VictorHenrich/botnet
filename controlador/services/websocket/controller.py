from typing import Type
from socketio import AsyncNamespace
from abc import ABC



class Controller(AsyncNamespace, ABC):
    async def on_connect(self, socketid: str, environ: Type) -> None:
        pass

    async def on_disconnect(self, socketid: str) -> None:
        pass