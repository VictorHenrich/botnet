from typing import Callable, Coroutine, Optional, Mapping, Any
import asyncio


from client.managers import ModuleManager
from client.websocket import SocketClient


class Client:
    def __init__(
        self,
        main_manager: ModuleManager,
        websocket: SocketClient
    ) -> None:
        self.__managers: ModuleManager = main_manager
        self.__websocket: SocketClient = websocket
        self.__listeners: list[Callable[[None], None]] = []

    @property
    def managers(self) -> ModuleManager:
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
    def __create_managers(cls, data: list[str]) -> ModuleManager:
        module_manager: ModuleManager = ModuleManager()
        
        for module in data:
            module_manager.create_task_manager(module)

        return module_manager

    @classmethod
    def create(
        cls,
        managers: list[str],
        websocket: Mapping[str, Any]
    ) -> Client:
        module_manager: ModuleManager = cls.__create_managers(managers)
        socket: SocketClient = cls.__create_websocket(websocket)

        return Client(module_manager, socket)
        





