# -*- coding: utf-8 -*-
'''
(c) Copyright 2014 Telefonica, I+D. Printed in Spain (Europe). All Rights
Reserved.

The copyright to the software program(s) is property of Telefonica I+D.
The program(s) may be used and or copied only with the express written
consent of Telefonica I+D or in accordance with the terms and conditions
stipulated in the agreement/contract under which the program(s) have
been supplied.
'''
from seleniumtid import selenium_driver
from seleniumtid.pageobjects.page_object import PageObject
from seleniumtid.pageelements.text_input_page_element import TextInputPageElement
from seleniumtid.pageelements.select_page_element import SelectPageElement
from examples.pageobjects import locators


class RegisterPageObject(PageObject):
    def __init__(self, driver=None):
        # Allow a second driver different from selenium_driver
        if driver:
            self.driver = driver
        else:
            self.driver = selenium_driver.driver

        self.username = TextInputPageElement(locators["register.username"], self.driver)
        self.password = TextInputPageElement(locators["register.password"], self.driver)
        self.name = TextInputPageElement(locators["register.name"], self.driver)
        self.email = TextInputPageElement(locators["register.email"], self.driver)
        self.place = SelectPageElement(locators["register.place"], self.driver)

        config = selenium_driver.config
        url = config.get('Common', 'url')
        self.driver.get(url)
        self.assertEqual(url, self.driver.current_url)

    def submit(self):
        self.driver.find_element(locators["register.submit"][0], locators["register.submit"][1]).click()
