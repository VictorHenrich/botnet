
import shlex
import sys
import subprocess
from dataclasses import dataclass
from typing import Type, Union, Mapping, Optional

from start import client
from client.managers import Task
from client.utils import UtilEnv



env_value: Mapping[str, Optional[str]] = UtilEnv.get_values()


@dataclass
class DataCommands:
    command: Union[str, list[str]]



@client.managers.add_task(env_value['MANAGER_AUTOMATE_SO'])
class RunShellCommands(Task):
    name: str = "executar_comandos"
    debug: bool = False
    data_class: Type[DataCommands] = DataCommands

    def __run_subprocess(self, commands: list[str]) -> None:
        active_windows_sheel: bool = "WIN" in sys.platform.upper()

        process: subprocess.CompletedProcess = subprocess.run(
            commands,
            shell=active_windows_sheel,
            text=True,
            stdout=subprocess.PIPE
        )

        print(f'\n==> {process.stdout}')

    def execute(self, data: DataCommands) -> None:
        if type(data.command) is list:
            commands: str = ' && '.join(data.command)

            self.__run_subprocess(shlex.split(commands))

        else:
            self.__run_subprocess(shlex.split(data.command))