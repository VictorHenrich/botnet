from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from typing import Any

from .. import AbstractDOMOperation, DOMOperations




class DOMOperationSubmit(AbstractDOMOperation):
    name: str = "submit"

    def operate(self, web_driver: WebDriver, web_element: WebElement, param: Any) -> None:
        web_element.submit()
        



DOMOperations.insert_operation(DOMOperationSubmit)
