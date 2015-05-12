# -*- coding: utf-8 -*-

u"""
(c) Copyright 2014 Telefónica, I+D. Printed in Spain (Europe). All Rights
Reserved.

The copyright to the software program(s) is property of Telefónica I+D.
The program(s) may be used and or copied only with the express written
consent of Telefónica I+D or in accordance with the terms and conditions
stipulated in the agreement/contract under which the program(s) have
been supplied.
"""

from selenium.webdriver.common.by import By

from seleniumtid.pageobjects.page_object import PageObject
from seleniumtid.pageelements import Text


class RegisterResultPageObject(PageObject):
    def init_page_elements(self):
        self.message = Text(By.XPATH, "//div[@id='content']/div/div/div/b[2]")
