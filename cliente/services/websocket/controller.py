from abc import ABC, abstractmethod
from socketio import ClientNamespace


class Controller(ClientNamespace, ABC):
    name: str

    @abstractmethod
    def on_connect(self) -> None:
        pass

    @abstractmethod
    def on_disconnect(self) -> None:
        pass