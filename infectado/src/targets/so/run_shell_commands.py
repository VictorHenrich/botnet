import subprocess
import sys
from dataclasses import dataclass
from typing import Type

from start import client
from services.managers import TargetManager



@dataclass
class DataCommands:
    command: str



class RunShellCommands(TargetManager):
    name: str = "executar_comandos"
    debug: bool = False
    data_class: Type[DataCommands]



    def execute(self, data: DataCommands) -> None:
        args: list[str] = data.command.split()

        active_windows_sheel: bool = sys.platform.upper() in "WIN"

        process: subprocess.CompletedProcess = \
            subprocess.run(args, capture_output=True, shell=active_windows_sheel)

        client.websocket.socket.emit('return_sheel', process.stdout.decode('utf-8'))



client.managers.get_manager('automacao_so').append_targets(RunShellCommands)