from dataclasses import dataclass
from services import server_client

@dataclass
class ObjectData:
    module: str
    targets: list[str]


@server_client.websocket.socket.on('on_controller')
def run_manager(data):
    objetoData: ObjectData = ObjectData(**data)

    server_client.manager_main.execute(
        objetoData.module,
        *objetoData.targets
    )