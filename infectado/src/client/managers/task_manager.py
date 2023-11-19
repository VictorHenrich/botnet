from typing import Any, Mapping, Optional, Sequence
from threading import Thread

from .abstract_command import AbstractCommand
from .task import Task


class TaskManager(AbstractCommand):
    def __init__(self, name: str) -> None:
        self.__name: str = name
        self.__tasks: Mapping[str, Task] = {}

    @property
    def name(self) -> str:
        return self.__name

    @property
    def tasks(self) -> Mapping[str, Task]:
        return self.__tasks

    def add_task(self, task: Task) -> None:
        self.__tasks[task.name] = task

    def execute(self, data: Optional[Any], *task_name: Sequence[str]) -> None:
        todo_list: list[Task] = [
            task for task in self.__tasks.values() if task.name in task_name
        ]

        threads: list[Thread] = [
            Thread(
                target=task.execute,
                args=(task.data_class(**data) if data and task.data_class else data,),
            )
            for task in todo_list
        ]

        [thread.start() for thread in threads]
        [thread.join() for thread in threads]
