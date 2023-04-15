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


class Tabs(TestCase):
    """This is the same test as test_android.py but without using Toolium"""
    def setUp(self):
        server_url = 'http://127.0.0.1:4723'

        capabilities = {
            'automationName': 'UiAutomator2',
            'platformName': 'Android',
            'deviceName': 'Android Emulator',
            'browserName': '',
            'app': 'https://github.com/appium/javascript-workshop/blob/master/apps/ApiDemos.apk?raw=true',
        }
        options = AppiumOptions()
        options.load_capabilities(capabilities)

        # Create a new appium driver before each test
        self.driver = webdriver.Remote(command_executor=server_url, options=options)
        self.driver.implicitly_wait(5)

    def tearDown(self):
        # Close driver
        self.driver.quit()

    def test_change_tab(self):
        # Open tabs activity
        option_locator = 'new UiScrollable(new UiSelector().scrollable(true).instance(0))' \
                         '.scrollIntoView(new UiSelector().text("{}").instance(0));'
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, option_locator.format('Views')).click()
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, option_locator.format('Tabs')).click()
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, option_locator.format('1. Content By Id')).click()

        # Check that the first tab is open
        content1 = self.driver.find_element(AppiumBy.ID, 'io.appium.android.apis:id/view1')
        assert 'tab1' == content1.text

        # Open second tab and check content
        self.driver.find_element(AppiumBy.XPATH, '(//android.widget.TabWidget//android.widget.TextView)[2]').click()
        content2 = self.driver.find_element(AppiumBy.ID, 'io.appium.android.apis:id/view2')
        assert 'tab2' == content2.text
