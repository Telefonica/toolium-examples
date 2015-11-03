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

from toolium_examples.test_cases import SeleniumTestCase
from toolium_examples.pageobjects.web.login import LoginPageObject


class Login(SeleniumTestCase):
    def test_successful_login_logout(self):
        user = {'username': 'tomsmith', 'password': 'SuperSecretPassword!'}
        expected_login_message = "You logged into a secure area!"
        expected_logout_message = "You logged out of the secure area!"

        # Open login form
        login_page = LoginPageObject().open()

        # Assert the full screen
        self.assertFullScreenshot('login_form')
        # Assert the full screen excluding a web element
        self.assertFullScreenshot('login_form_no_password', exclude_elements=[login_page.password])
        # Assert only a web element
        self.assertScreenshot(login_page.login_button, 'login_submit_button')

        # Login and check welcome message
        secure_area = login_page.login(user)
        self.assertIn(expected_login_message, secure_area.message.get_message())

        # Assert the full screen
        self.assertFullScreenshot('login_secure_area')

        # Logout and check logout message
        login_page = secure_area.logout()
        self.assertIn(expected_logout_message, login_page.message.get_message())

        # Assert the full screen
        self.assertFullScreenshot('login_logout')
