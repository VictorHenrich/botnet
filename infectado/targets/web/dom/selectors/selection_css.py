from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from typing import Union

from .. import AbstractDOMSelection, DOMSelections




class DOMSelectionByCSS(AbstractDOMSelection):
    name: str = "css"
    
    def get_by(self, web: Union[WebDriver, WebElement], identifier: str) -> WebElement:
        return web.find_element(By.CSS_SELECTOR, identifier)



DOMSelections.insert_selection(DOMSelectionByCSS)
