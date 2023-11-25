from typing import Type
from server import Server
from server.websocket import Controller


@Server.websocket.on("/bots")
class BotController(Controller):
    async def on_connect(self, socketid: str, environ: Type) -> None:
        pass
