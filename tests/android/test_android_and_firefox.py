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

from toolium.driver_wrapper import DriverWrapper
from toolium_examples.pageobjects.android.menu import MenuPageObject
from toolium_examples.pageobjects.android.tabs import TabsPageObject
from toolium_examples.pageobjects.web.login import LoginPageObject
from toolium_examples.test_cases import AndroidTestCase


class TwoDrivers(AndroidTestCase):
    def test_change_tab_and_successful_login(self):
        # Create a second driver
        second_wrapper = DriverWrapper()
        second_wrapper.config.set('Browser', 'browser', 'firefox')
        second_wrapper.connect()

        # [Mobile] Open tabs activity
        MenuPageObject().open_option('Views').open_option('Tabs').open_option('1. Content By Id')
        tabs_page = TabsPageObject()
        self.assertEqual('tab1', tabs_page.content1.text)

        # [Web] Login and check welcome message
        user = {'username': 'tomsmith', 'password': 'SuperSecretPassword!'}
        expected_login_message = "You logged into a secure area!"
        expected_logout_message = "You logged out of the secure area!"
        secure_area = LoginPageObject(second_wrapper).open().login(user)
        self.assertIn(expected_login_message, secure_area.message.get_message())

        # [Mobile] Open second tab and check content
        tabs_page.tab2.click()
        self.assertEqual('tab2', tabs_page.content2.text)

        # [Web] Logout and check logout message
        login_page = secure_area.logout()
        self.assertIn(expected_logout_message, login_page.message.get_message())
