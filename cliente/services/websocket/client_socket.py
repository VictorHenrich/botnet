from socketio import AsyncClient

from services.websocket import Controller



class ClientSocket:
    def __init__(
        self,
        url_connection: str
    ) -> None:
        self.__socket: AsyncClient = AsyncClient()
        self.__url: str = url_connection

    @property
    def socket(self) -> AsyncClient:
        return self.__socket

    async def start(self) -> None:
        await self.__socket.connect(self.__url)

    async def close(self) -> None:
        await self.__socket.disconnect()

    def register_controller(self, controller: Controller):
        self.__socket.register_namespace(controller(controller.name))
