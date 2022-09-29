from dataclasses import dataclass
from typing import Any, Optional
from services import client

@dataclass
class ObjectData:
    module: str
    targets: list[str]
    args: Optional[Any] = None


@client.websocket.socket.on('on_controller')
def run_manager(data):
    objetoData: ObjectData = ObjectData(**data)

    client.manager_main.execute(
        objetoData.module,
        objetoData.args
        *objetoData.targets
    )