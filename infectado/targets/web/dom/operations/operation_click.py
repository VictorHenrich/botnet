from selenium.webdriver.remote.webelement import WebElement
from typing import Any

from .. import AbstractDOMOperation




class DOMOperationWrite(AbstractDOMOperation):
    def operate(self, web_element: WebElement, param: Any) -> None:
        web_element.click()