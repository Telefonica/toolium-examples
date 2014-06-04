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
from selenium_tid_python import selenium_driver
from selenium_tid_python.pageobjects.page_object import PageObject
from selenium_tid_python.pageelements.text_input_page_element import TextInputPageElement
from selenium_tid_python.pageelements.select_page_element import SelectPageElement
from selenium_python.pageobjects import locators


class UsernameElement(TextInputPageElement):
    def __init__(self):
        self.locator = locators["register.username"]


class PasswordElement(TextInputPageElement):
    def __init__(self):
        self.locator = locators["register.password"]


class NameElement(TextInputPageElement):
    def __init__(self):
        self.locator = locators["register.name"]


class EmailElement(TextInputPageElement):
    def __init__(self):
        self.locator = locators["register.email"]


class PlaceElement(SelectPageElement):
    def __init__(self):
        self.locator = locators["register.place"]


class RegisterPageObject(PageObject):
    username = UsernameElement()
    password = PasswordElement()
    name = NameElement()
    email = EmailElement()
    place = PlaceElement()

    def __init__(self):
        self.driver = selenium_driver.driver
        config = selenium_driver.config
        url = config.get('Common', 'url')
        self.driver.get(url)
        self.assertEqual(url, self.driver.current_url)

    def submit(self):
        self.driver.find_element(locators["register.submit"][0], locators["register.submit"][1]).click()
