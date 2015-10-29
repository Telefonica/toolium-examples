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
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class Tabs(TestCase):
    def setUp(self):
        server_url = 'http://127.0.0.1:4723/wd/hub'

        capabilities = DesiredCapabilities.ANDROID
        capabilities['automationName'] = 'Appium'
        capabilities['platformName'] = 'Android'
        capabilities['deviceName'] = 'Android Emulator'
        capabilities['browserName'] = ''
        capabilities['app'] = 'https://github.com/appium/javascript-workshop/blob/master/apps/ApiDemos.apk?raw=true'
        capabilities['appWaitActivity'] = ''

        # Create a new appium driver before each test
        self.driver = WebDriver(command_executor=server_url, desired_capabilities=capabilities)
        self.driver.implicitly_wait(5)

    def tearDown(self):
        # Close driver
        self.driver.quit()

    def test_change_tab(self):
        # Open tabs activity
        option_locator = 'new UiScrollable(new UiSelector().scrollable(true).instance(0))' \
                         '.scrollIntoView(new UiSelector().text("{}").instance(0));'
        self.driver.find_element_by_android_uiautomator(option_locator.format('Views')).click()
        self.driver.find_element_by_android_uiautomator(option_locator.format('Tabs')).click()
        self.driver.find_element_by_android_uiautomator(option_locator.format('1. Content By Id')).click()

        # Check that the first tab is open
        content1 = self.driver.find_element_by_id('io.appium.android.apis:id/view1')
        self.assertEqual('tab1', content1.text)

        # Open second tab and check content
        self.driver.find_element_by_xpath('(//android.widget.TabWidget//android.widget.TextView)[2]').click()
        content2 = self.driver.find_element_by_id('io.appium.android.apis:id/view2')
        self.assertEqual('tab2', content2.text)
