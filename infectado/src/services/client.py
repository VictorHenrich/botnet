from typing import Callable, Coroutine, Optional, Mapping, Any
import asyncio

from services.managers import MainManager, Manager
from services.websocket import SocketClient


class Client:
    def __init__(
        self,
        main_manager: MainManager,
        websocket: SocketClient
    ) -> None:
        self.__managers: MainManager = main_manager
        self.__websocket: SocketClient = websocket
        self.__listeners: list[Callable[[None], None]] = []

    @property
    def managers(self) -> MainManager:
        return self.__managers

    @property
    def websocket(self) -> SocketClient:
        return self.__websocket

    @property
    def listeners(self) -> list[Callable[[None], None]]:
        return self.__listeners

    def start(self, function: Callable[[None], None])  -> Callable[[None], None]:
        self.__listeners.append(function)

        return function

    def start_client(self) -> None:
        for function in self.__listeners:
            result: Optional[Coroutine] = function()

            if isinstance(result, Coroutine):
                asyncio.run(result)



class ClientFactory:
    @classmethod
    def __create_websocket(cls, data: Mapping[str, Any]) -> SocketClient:
        socket_client: SocketClient = SocketClient(
            data['url'], 
            data.get('namespaces') or []
        )

        return socket_client

    @classmethod
    def __create_managers(cls, data: list[str]) -> MainManager:
        main_manager: MainManager = MainManager()
        
        for manager in data:
            main_manager.append_managers(Manager(manager))

        return main_manager

    @classmethod
    def create(
        cls,
        managers: list[str],
        websocket: Mapping[str, Any]
    ) -> Client:
        main_manager: MainManager = cls.__create_managers(managers)
        socket: SocketClient = cls.__create_websocket(websocket)

        return Client(main_manager, socket)
        





