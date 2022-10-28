from typing import Callable, Coroutine, Optional
import asyncio
from pydantic import BaseModel, validate_arguments

from services.managers.manager_main import ManagerMain
from services.websocket.client_socket import ClientSocket


class Client(BaseModel):
    manager_main: ManagerMain
    websocket: ClientSocket
    listeners: list[Callable[[None], None]] = []

    @validate_arguments
    def start(self, function: Callable[[None], None])  -> Callable[[None], None]:
        self.listeners.append(function)

        return function

    def start_client(self) -> None:
        for function in self.listeners:
            result: Optional[Coroutine] = function()

            if isinstance(result, Coroutine):
                asyncio.run(result)





