from abc import ABC
from pathlib import Path
from typing import Any, Mapping, Sequence, Union, Type, Union
from selenium.webdriver.remote.webdriver import WebDriver



class AbstractDrive(ABC):
    name_executable: Union[Path, str]
    name: str
    class_: Type[WebDriver]

    @classmethod
    def get_browser(cls, *args: Sequence[Any], **kwargs: Mapping[str, Any]) -> WebDriver:
        return cls.class_(*args, **kwargs)