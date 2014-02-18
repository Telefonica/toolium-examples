from pageobjects.common import selenium_driver
from pageobjects.common.page_object import PageObject
from pageobjects.common.text_page_element import TextPageElement
from pageobjects.common.select_page_element import SelectPageElement
from pageobjects import locators


class MessageElement(TextPageElement):
    def __init__(self):
        self.locator = locators["register.result.message"]


class RegisterResultPageObject(PageObject):
    message = MessageElement()

    def __init__(self):
        self.driver = selenium_driver.driver
