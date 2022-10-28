from typing import Optional, Type
from socketio import AsyncNamespace
from abc import ABC



class Controller(AsyncNamespace, ABC):
    def __init__(self, namespace:Optional[str] = None):
        self.__connected_list: list[str] = []

        super().__init__(namespace)

    @property
    def connected_list(self) -> list[str]:
        return self.__connected_list

    async def on_connect(self, socketid: str, environ: Type) -> None:
        self.__connected_list.append(socketid)

    async def on_disconnect(self, socketid: str) -> None:
        self.__connected_list.remove(socketid)