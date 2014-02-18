from pageobjects.common import selenium_driver
from pageobjects.common.page_element import PageElement


class TextPageElement(PageElement):
    def __get__(self, obj, cls=None):
        driver = selenium_driver.driver
        return driver.find_element(self.locator[0], self.locator[1]).text
