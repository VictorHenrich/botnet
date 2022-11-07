from typing import Callable, Coroutine, Optional, Mapping, Any
import asyncio

from services.managers import MainManager
from services.websocket import SocketClient


class Client:
    listeners: list[Callable[[None], None]] = []

    def __init__(
        self,
        main_manager: MainManager,
        websocket: SocketClient
    ) -> None:
        self.__manager: MainManager = main_manager
        self.__websocket: SocketClient = websocket

    @property
    def manager(self) -> MainManager:
        return self.__manager

    @property
    def websocket(self) -> SocketClient:
        return self.__websocket

    def start(self, function: Callable[[None], None])  -> Callable[[None], None]:
        self.listeners.append(function)

        return function

    def start_client(self) -> None:
        for function in self.listeners:
            result: Optional[Coroutine] = function()

            if isinstance(result, Coroutine):
                asyncio.run(result)



class ClientFactory:
    @classmethod
    def create(
        cls,
        managers: list[str],
        websocket: Mapping[str, Any]
    ) -> Client:
        pass





