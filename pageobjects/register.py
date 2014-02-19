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
from pageobjects.common import selenium_driver
from pageobjects.common.page_object import PageObject
from pageobjects.common.text_input_page_element import TextInputPageElement
from pageobjects.common.select_page_element import SelectPageElement
from pageobjects import locators


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
        url = "http://qacore01.hi.inet/sites/seleniumExamples/register.html"
        self.driver.get(url)
        self.assertEqual(url, self.driver.current_url)

    def submit(self):
        self.driver.find_element(locators["register.submit"][0], locators["register.submit"][1]).click()
