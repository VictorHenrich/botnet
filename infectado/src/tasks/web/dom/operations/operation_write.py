from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from time import sleep

from .. import AbstractDOMOperation, DOMOperations


class DOMOperationWrite(AbstractDOMOperation):
    name: str = "write"

    def operate(
        self, web_driver: WebDriver, web_element: WebElement, param: str
    ) -> None:
        web_element.send_keys(param)

        sleep(2)


DOMOperations.insert_operation(DOMOperationWrite)
