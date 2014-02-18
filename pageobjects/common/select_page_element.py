from pageobjects.common import selenium_driver
from pageobjects.common.page_element import PageElement
from selenium.webdriver.support.ui import Select


class SelectPageElement(PageElement):
    def __get__(self, obj, cls=None):
        driver = selenium_driver.driver
        return Select(driver.find_element(self.locator[0], self.locator[1])).first_selected_option.text

    def __set__(self, obj, val):
        driver = selenium_driver.driver
        Select(driver.find_element(self.locator[0], self.locator[1])).select_by_visible_text(val)
