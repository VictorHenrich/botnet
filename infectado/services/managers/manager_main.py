from typing import Mapping, Sequence
from .abstract_manager import AbstractManager
from .manager import Manager


class ManagerMain(AbstractManager):

    def __init__(self):
        self.__managers: Mapping[str, Manager] = {}

    @property
    def managers(self) -> Mapping[str, Manager]:
        return self.__managers

    def get_manager(self, manager_name: str) -> Manager:
        return self.__managers[manager_name]

    def append_managers(self, *managers: Sequence[Manager]) -> None:
        for manager in managers:
            self.__managers[manager.name] = manager

    def execute(self, manager_name: str, *targets_name: Sequence[str]):
        for manager in self.__managers.values():
            if manager.name.upper() == manager_name.upper():
                manager.execute(*targets_name)
                return

        raise Exception('Manager not found!')