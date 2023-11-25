from server import Server
from utils.types import DictType


class ControlBotsService:
    def __init__(self, payload: DictType) -> None:
        self.__payload: DictType = payload

    async def execute(self) -> None:
        await Server.websocket.socket.emit(
            "controle", self.__payload, namespace="/bots"
        )
