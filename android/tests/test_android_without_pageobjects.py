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

from android.test_cases import AndroidTestCase
from selenium.webdriver.common.by import By

class Tabs(AndroidTestCase):
    """This is the same test as test_android.py but without using page objects"""

    def test_change_tab(self):
        # Open tabs activity
        option_locator = 'new UiScrollable(new UiSelector().scrollable(true).instance(0))' \
                         '.scrollIntoView(new UiSelector().text("{}").instance(0));'
        self.driver.find_element_by_android_uiautomator(option_locator.format('Views')).click()
        self.driver.find_element_by_android_uiautomator(option_locator.format('Tabs')).click()
        self.driver.find_element_by_android_uiautomator(option_locator.format('1. Content By Id')).click()

        # Check that the first tab is open
        content1 = self.driver.find_element(By.ID, 'io.appium.android.apis:id/view1')
        assert 'tab1' == content1.text

        # Open second tab and check content
        self.driver.find_element(By.XPATH, '(//android.widget.TabWidget//android.widget.TextView)[2]').click()
        content2 = self.driver.find_element(By.ID, 'io.appium.android.apis:id/view2')
        assert 'tab2' == content2.text
