from typing import Callable, Coroutine, Union
import asyncio

from .http.server_http import ServerHttp
from .websocket.server_socket import ServerSocket


class Server:
    def __init__(
        self,
        http: ServerHttp,
        websocket: ServerSocket 
    ) -> None:
        self.__http: ServerHttp = http
        self.__websocket: ServerSocket = websocket
        self.__listeners: list[Callable[[None], None]] = []

    @property
    def http(self) -> ServerHttp:
        return self.__http

    @property
    def websocket(self) -> ServerSocket:
        return self.__websocket

    def start(self, function: Callable[[None], None]) -> Callable[[None], None]:
        self.__listeners.append(function)

        return function

    def start_server(self) -> None:
        for function in self.__listeners:
            result: Union[Coroutine, None] = function()

            if isinstance(result, Coroutine):
                asyncio.run(result)
                