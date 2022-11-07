from typing import Callable, Type
from socketio import AsyncServer

from services.http import HttpServer
from .controller import Controller


class SocketServer:
    def __init__(self, http: HttpServer) -> None:
        self.__socket: AsyncServer = AsyncServer()

        self.__socket.attach(http.app)

    def on(self, event_name: str) -> Callable[[Type[Controller]], None]:
        def wrapper(controller_class: Type[Controller]) -> None:
            self.__socket.register_namespace(controller_class(event_name))

        return wrapper

    @property
    def socket(self) -> AsyncServer:
        return self.__socket
