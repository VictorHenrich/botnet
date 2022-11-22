from typing import Any, Mapping, Optional, Sequence, Type
from threading import Thread


from .abstract_manager import AbstractManager
from .target_manager import TargetManager


class Manager(AbstractManager):
    def __init__(self, name: str) -> None:
        self.__name: str = name
        self.__targets: Mapping[str, TargetManager] = {}

    @property
    def name(self) -> str:
        return self.__name

    @property
    def targets(self) -> Mapping[str, TargetManager]:
        return self.__targets

    def append_targets(self, *targets: Sequence[Type[TargetManager]]) -> None:
        for target in targets:
            self.targets[target.name] = target()

    def execute(self, data: Optional[Any], *targets: Sequence[str]) -> None:
        list_targets: list[TargetManager] = [
            target
            for target in self.targets.values()
            if target.name in targets
        ]

        threads: list[Thread] = [
            Thread(
                target=target.execute,
                args=(
                    target.data_class(**data) \
                        if data and target.data_class \
                        else data
                    ,
                )
            )

            for target in list_targets
        ]

        [thread.start() for thread in threads]
        [thread.join() for thread in threads]


    

    
