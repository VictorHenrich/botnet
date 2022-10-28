from typing import Any, Mapping, Optional, Sequence, Type
from threading import Thread
from pydantic import BaseModel, validator, validate_arguments

from .abstract_manager import AbstractManager
from .manager_target import ManagerTarget


class Manager(AbstractManager, BaseModel):
    name: str
    targets: Mapping[str, ManagerTarget] = {}

    @validator('targets', pre=True)
    def handle_targerts(cls, value: Sequence[Type[ManagerTarget]]) -> Mapping[str, ManagerTarget]:
        if not value:
            return {}

        return {
            target.name: target()
            for target in value
        }

    @validate_arguments
    def append_targets(self, *targets: Sequence[Type[ManagerTarget]]) -> None:
        for target in targets:
            self.targets[target.name] = target()

    @validate_arguments
    def execute(self, data: Optional[Any], *targets: Sequence[str]) -> None:
        list_targets: list[ManagerTarget] = [
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


    

    
