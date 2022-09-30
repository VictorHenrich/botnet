from socketio import Client

from services.websocket import Controller



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
        print(f' CLIENT CONNECT IN {self.__url} '.center(100, '-'))

    def close(self) -> None:
        self.__socket.disconnect()
        print(f' CLIENT DISCONNECT IN {self.__url} '.center(100, '-'))

    def register_controller(self, controller: Controller):
        self.__socket.register_namespace(controller(controller.name))
