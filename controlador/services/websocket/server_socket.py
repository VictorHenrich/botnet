from socketio import AsyncServer
from services.http.server_http import ServerHttp


class ServerSocket:
    def __init__(self, app: ServerHttp) -> None:
        self.__socket: AsyncServer = AsyncServer()

        self.__socket.attach(app)

    @property
    def socket(self) -> AsyncServer:
        return self.__socket
