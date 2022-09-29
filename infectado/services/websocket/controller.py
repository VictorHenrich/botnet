from abc import ABC, abstractmethod
<<<<<<< HEAD
from socketio import ClientNamespace


class Controller(ClientNamespace, ABC):
    name: str

    @abstractmethod
    def on_connect(self) -> None:
        pass

    @abstractmethod
    def on_disconnect(self) -> None:
=======
from socketio import AsyncClientNamespace


class Controller(AsyncClientNamespace, ABC):
    name: str

    @abstractmethod
    async def on_connect(self) -> None:
        pass

    @abstractmethod
    async def on_disconnect(self) -> None:
>>>>>>> cliente
        pass