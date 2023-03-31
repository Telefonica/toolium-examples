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

from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class IosTestApp(TestCase):
    """This is the same test as test_ios.py but without using Toolium"""

    def setUp(self):
        server_url = 'http://127.0.0.1:4723/wd/hub'
        app = 'https://github.com/appium/javascript-workshop/blob/master/apps/TestApp7.1.app.zip?raw=true&fake=.zip'

        capabilities = DesiredCapabilities.IPHONE
        capabilities['automationName'] = 'XCUITest'
        capabilities['platformName'] = 'iOS'
        capabilities['deviceName'] = 'iPhone 7'
        capabilities['platformVersion'] = '10.0'
        capabilities['browserName'] = ''
        capabilities['app'] = app
        # Create a new appium driver before each test
        self.driver = WebDriver(command_executor=server_url, desired_capabilities=capabilities)
        self.driver.implicitly_wait(5)

    def tearDown(self):
        # Close driver
        self.driver.quit()

    def test_sum(self):
        first_number = 2
        second_number = 3

        # Input numbers and click button
        first_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//UIATextField[1]")))
        first_element.send_keys(first_number)
        self.driver.find_element(By.XPATH, "//UIATextField[2]").send_keys(second_number)
        self.driver.find_element_by_accessibility_id("ComputeSumButton").click()

        # Check expected result
        result = int(self.driver.find_element(By.XPATH, "//UIAStaticText[1]").text)
        assert first_number + second_number == result, "Wrong sum"
