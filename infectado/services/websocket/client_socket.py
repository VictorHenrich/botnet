from socketio import Client



class ClientSocket:
    def __init__(
        self,
        url_connection: str
    ) -> None:
        self.__socket: Client = Client()
        self.__url: str = url_connection

    @property
    def socket(self) -> Client:
        return self.__socket

    def start(self) -> None:
        self.__socket.connect(self.__url)

    def close(self) -> None:
        self.__socket.disconnect()