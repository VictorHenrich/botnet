from socketio import Client

from services.websocket import Controller



class ClientSocket:
    def __init__(
        self,
        url_connection: str,
        namespaces: list[str] = []
    ) -> None:
        self.__socket: Client = Client()
        self.__url: str = url_connection
        self.__namespaces: list[str] = namespaces

    @property
    def socket(self) -> Client:
        return self.__socket

    def start(self) -> None:
        self.__socket.connect(self.__url, namespaces=self.__namespaces)
        print(f' CLIENT CONNECT IN {self.__url} '.center(100, '-'))

    def close(self) -> None:
        self.__socket.disconnect()
        print(f' CLIENT DISCONNECT IN {self.__url} '.center(100, '-'))
