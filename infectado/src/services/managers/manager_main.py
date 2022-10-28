from typing import Any, Mapping, Optional, Sequence
from pydantic import validate_arguments, BaseModel
from .abstract_manager import AbstractManager
from .manager import Manager


class ManagerMain(AbstractManager, BaseModel):
    managers: Mapping[str, Manager] = {}

    @validate_arguments
    def get_manager(self, manager_name: str) -> Manager:
        return self.managers[manager_name]

    @validate_arguments
    def append_managers(self, *managers: Sequence[Manager]) -> None:
        for manager in managers:
            self.managers[manager.name] = manager

    @validate_arguments
    def execute(self, manager_name: str, data: Optional[Any], *targets_name: Sequence[str]) -> None:
        for manager in self.managers.values():
            if manager.name.upper() == manager_name.upper():
                manager.execute(data, *targets_name)
                return

        raise Exception('Manager not found!')