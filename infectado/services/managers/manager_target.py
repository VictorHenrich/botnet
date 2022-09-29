from typing import Any, Optional
from .abstract_manager import AbstractManager
from abc import ABC, abstractmethod


class ManagerTarget(AbstractManager, ABC):
    name: str
    debug: bool = False

    def __init__(self) -> None:
        self.__name = self.__class__.name
        self.__debug = self.__class__.debug


        if not self.__name:
            raise Exception(f"class {self.__class__.__name__} no name has been defined")

    @property
    def name(self) -> str:
        return self.__name

    @property
    def debug(self) -> bool:
        return self.__debug

    @abstractmethod
    def execute(self, data: Optional[Any]):
        pass