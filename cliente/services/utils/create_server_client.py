from services.client.server_client import ServerClient
from services.managers.manager_main import ManagerMain, Manager
from services.websocket.client_socket import ClientSocket



def create_server_client(url: str, managers: list[Manager]) -> ServerClient:
    manager_main: ManagerMain = ManagerMain()
    client_socket: ClientSocket = ClientSocket(url)

    manager_main.append_managers(*managers)

    return ServerClient(
        manager_main,
        client_socket
    )