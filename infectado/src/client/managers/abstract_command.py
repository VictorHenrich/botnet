from abc import ABC, abstractmethod
from typing import Sequence, Mapping, Any



class AbstractCommand(ABC):
    @abstractmethod
    def execute(self, *args: Sequence[Any], **kwargs: Mapping[str, Any]) -> None:
        pass