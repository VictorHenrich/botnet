from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from typing import Any

from .. import AbstractDOMOperation, DOMOperations


class DOMOperationClick(AbstractDOMOperation):
    name: str = "click"

    def operate(
        self, web_driver: WebDriver, web_element: WebElement, param: Any
    ) -> None:
        web_element.click()


DOMOperations.insert_operation(DOMOperationClick)
