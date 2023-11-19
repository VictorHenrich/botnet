from socketio import Client
from typing import Type, Callable
from client.websocket import Controller


class SocketClient:
    def __init__(self, url_connection: str, namespaces: list[str] = []) -> None:
        self.__url: str = url_connection
        self.__namespaces: list[str] = namespaces
        self.__socket: Client = Client(url_connection)

    @property
    def url(self) -> str:
        return self.__url

    @property
    def namespaces(self) -> list[str]:
        return self.__namespaces

    @property
    def socket(self) -> Client:
        return self.__socket

    def on(self, event_name: str) -> Callable[[Type[Controller]], None]:
        def wrapper(controller_class: Type[Controller]) -> None:
            self.__socket.register_namespace(controller_class(event_name))

        return wrapper

    def start(self) -> None:
        self.__socket.connect(self.__url, namespaces=self.__namespaces)
        print(f" CLIENT CONNECT IN {self.__url} ".center(100, "-"))

    def close(self) -> None:
        self.__socket.disconnect()
        print(f" CLIENT DISCONNECT IN {self.__url} ".center(100, "-"))
