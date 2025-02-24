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

from unittest import TestCase

from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class IosTestApp(TestCase):
    """This is the same test as test_ios.py but without using Toolium"""

    def setUp(self):
        server_url = 'http://127.0.0.1:4723/wd/hub'
        app = 'https://github.com/appium/ios-uicatalog/blob/master/UIKitCatalog/UIKitCatalog-iphonesimulator.zip?raw=true'

        capabilities = {
            'platformName': 'iOS',
            'browserName': '',
            'appium:automationName': 'XCUITest',
            'appium:platformVersion': '17.5',
            'appium:deviceName': 'iPhone 15',
            'appium:app': app,
        }
        options = AppiumOptions()
        options.load_capabilities(capabilities)

        # Create a new appium driver before each test
        self.driver = webdriver.Remote(command_executor=server_url, options=options)
        self.driver.implicitly_wait(5)

    def tearDown(self):
        # Close driver
        self.driver.quit()

    def test_alert_is_shown_no_toolium(self):
        # Open alert view
        alert_view = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.IOS_PREDICATE, 'label == "Alert Views"')))
        alert_view.click()

        # Click on Simple alert
        self.driver.find_element(AppiumBy.IOS_PREDICATE, 'label == "Simple"').click()

        # Check expected result
        alert = self.driver.find_element(AppiumBy.CLASS_NAME, 'XCUIElementTypeAlert')
       
        assert alert.is_displayed(), 'Alert is not shown'
