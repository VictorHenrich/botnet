from services.client import Client
from services.managers.manager_main import ManagerMain, Manager
from services.websocket.client_socket import ClientSocket



def create_client(url: str, managers: list[str]) -> Client:
    manager_main: ManagerMain = ManagerMain()
    client_socket: ClientSocket = ClientSocket(url)

    managers_: list[Manager] = [
        Manager(manager_name)
        for manager_name in managers 
    ]

    manager_main.append_managers(*managers_)

    return Client(
        manager_main,
        client_socket
    )