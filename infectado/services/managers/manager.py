from typing import Any, Mapping, Optional, Sequence, Type

from .abstract_manager import AbstractManager
from .manager_target import ManagerTarget


class Manager(AbstractManager):
    def __init__(self, name: str) -> None:
        self.__name: str = name
        self.__targets: Mapping[str, ManagerTarget] = {}

    @property
    def name(self) -> str:
        return self.__name

    @property
    def targets(self) -> Mapping[str, ManagerTarget]:
        return self.__targets

    def append_targets(self, *targets: Sequence[Type[ManagerTarget]]) -> None:
        for target in targets:
            self.__targets[target.name] = target()

    def execute(self, data: Optional[Any], *targets: Sequence[str]):
        for target in self.__targets.values():
            if target.name in targets:
                object_data: Optional[Any] = \
                    target.data_class(**data) \
                        if data and target.data_class \
                        else data

                target.execute(object_data)


    

    
