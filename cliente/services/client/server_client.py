from typing import Callable

from services.managers.manager_main import ManagerMain
from services.websocket.client_socket import ClientSocket


class ServerClient:
    def __init__(
        self,
        manager_main: ManagerMain,
        websocket: ClientSocket
    ) -> None:
        self.__manager_main: ManagerMain = manager_main
        self.__websocket: ClientSocket = websocket
        self.__listeners: list[Callable[[None], None]] = []

    @property
    def manager_main(self) -> ManagerMain:
        return self.__manager_main

    @property
    def websocket(self) -> ClientSocket:
        return self.__websocket

    def start(self, function: Callable[[None], None])  -> Callable[[None], None]:
        self.__listeners.append(function)

        return function

    def start_server(self) -> None:
        for function in self.__listeners:
            function()




