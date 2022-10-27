from abc import ABC
from socketio import ClientNamespace


class Controller(ClientNamespace, ABC):
    def on_connect(self) -> None:
        pass

    def on_disconnect(self) -> None:
        pass
