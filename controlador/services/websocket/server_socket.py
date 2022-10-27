from typing import Callable, Type
from socketio import AsyncServer

from services.http.server_http import ServerHttp
from .controller import Controller


class ServerSocket:
    def __init__(self, http: ServerHttp) -> None:
        self.__socket: AsyncServer = AsyncServer()

        self.__socket.attach(http.app)

    def on(self, event_name: str) -> Callable[[Type[Controller]], None]:
        def wrapper(controller_class: Type[Controller]) -> None:
            self.__socket.register_namespace(controller_class(event_name))

        return wrapper

    @property
    def socket(self) -> AsyncServer:
        return self.__socket
