from pageobjects.common import selenium_driver
from pageobjects.common.page_element import PageElement


class TextInputPageElement(PageElement):
    def __get__(self, obj, cls=None):
        driver = selenium_driver.driver
        return driver.find_element(self.locator[0], self.locator[1]).get_attribute("value")

    def __set__(self, obj, val):
        driver = selenium_driver.driver
        driver.find_element(self.locator[0], self.locator[1]).send_keys(val)
