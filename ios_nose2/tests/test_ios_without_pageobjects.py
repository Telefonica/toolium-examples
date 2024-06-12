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

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from ios_nose2.test_cases import IosTestCase


class IosTestApp(IosTestCase):
    """This is the same test as test_ios.py but without using page objects"""

    def test_alert_is_shown_no_pageobject(self):
        # Open alert view
        alert_view = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.IOS_PREDICATE, 'label == "Alert Views"')))
        alert_view.click()

        # Click on Simple alert
        self.driver.find_element(AppiumBy.IOS_PREDICATE, 'label == "Simple"').click()

        # Check expected result
        alert = self.driver.find_element(AppiumBy.CLASS_NAME, 'XCUIElementTypeAlert')
       
        assert alert.is_displayed(), 'Alert is not shown'
