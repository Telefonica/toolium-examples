# -*- coding: utf-8 -*-
u"""
Copyright 2015 Telefónica Investigación y Desarrollo, S.A.U.
This file is part of Toolium.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy

from toolium.pageobjects.page_object import PageObject
from toolium.pageelements import *


class CalcPageObject(PageObject):
    first_op = InputText(By.XPATH, '//XCUIElementTypeTextField[1]')
    second_op = InputText(By.XPATH, '//XCUIElementTypeTextField[2]')
    compute = Button(MobileBy.ACCESSIBILITY_ID, 'ComputeSumButton')
    result = Text(By.XPATH, '//XCUIElementTypeStaticText[1]')
    status_bar = PageElement(By.XPATH, '//XCUIElementTypeStatusBar[1]')

    def sum(self, first_number, second_number):
        """Add two numbers

        :param first_number: first value
        :param second_number: second value
        :returns: calc page object
        """
        self.first_op.wait_until_visible()
        self.first_op.text = first_number
        self.second_op.text = second_number
        self.driver.hide_keyboard(key_name='Done')
        self.compute.click()
        return self

    def get_sum_result(self):
        """Get sum result from calculator

        :returns: int with sum result
        """
        return int(self.result.text)
