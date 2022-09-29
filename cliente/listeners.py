from dataclasses import dataclass
from services import client

@dataclass
class ObjectData:
    module: str
    targets: list[str]


@client.websocket.socket.on('on_controller')
def run_manager(data):
    objetoData: ObjectData = ObjectData(**data)

    client.manager_main.execute(
        objetoData.module,
        *objetoData.targets
    )