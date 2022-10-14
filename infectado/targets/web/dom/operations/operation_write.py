from selenium.webdriver.remote.webelement import WebElement
from typing import Any

from .. import AbstractDOMOperation




class DOMOperationWrite(AbstractDOMOperation):
    def operate(self, web_element: WebElement, param: str) -> None:
        web_element.send_keys(param)