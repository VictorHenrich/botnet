from typing import Any, Mapping, Optional, Sequence, Type
from .abstract_command import AbstractCommand
from .task_manager import TaskManager
from .task import Task


class ModuleManager(AbstractCommand):
    def __init__(self) -> None:
        self.__modules: Mapping[str, TaskManager] = {}

    @property
    def modules(self) -> Mapping[str, TaskManager]:
        return self.__modules

    def add_task(self, module_name: str) -> TaskManager:
        def wrapper(cls: Type[Task]) -> Type[Task]:
            task_manager: TaskManager = self.__modules[module_name]

            task_manager.add_task(cls())

            return cls

        return wrapper

    def create_task_manager(self, name: str) -> None:
        task_manager: TaskManager = TaskManager(name)

        self.__modules[task_manager.name] = task_manager

    def execute(
        self, module_name: str, data: Optional[Any], *task_name: Sequence[str]
    ) -> None:
        for manager in self.__modules.values():
            if manager.name.upper() == module_name.upper():
                manager.execute(data, *task_name)
                return

        raise Exception("TaskManager not found!")
