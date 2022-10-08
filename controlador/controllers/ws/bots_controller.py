from typing import Type
from services import server
from services.websocket import Controller


@server.websocket.on('/bots')
class BotsController(Controller):
    async def on_connect(self, socketid: str, environ: Type) -> None:
        pass