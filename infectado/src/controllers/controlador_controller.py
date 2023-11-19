from dataclasses import dataclass
from typing import Any, Optional
from start import client
from client.websocket import Controller


@dataclass
class ObjectData:
    module: str
    targets: list[str]
    args: Optional[Any] = None


@client.websocket.on("/bots")
class ControladorController(Controller):
    def on_controle(self, data):
        objetoData: ObjectData = ObjectData(**data)

        client.managers.execute(objetoData.module, objetoData.args, *objetoData.targets)
