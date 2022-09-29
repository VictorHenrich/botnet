from abc import ABC, abstractmethod
from socketio import AsyncClientNamespace


class Controller(AsyncClientNamespace, ABC):
    name: str

    @abstractmethod
    async def on_connect(self) -> None:
        pass

    @abstractmethod
    async def on_disconnect(self) -> None:
        pass