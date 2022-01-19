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

from nose.tools import assert_in

from web.pageobjects.login import LoginPageObject
from web.test_cases import SeleniumTestCase
from selenium.webdriver.common.by import By


class Login(SeleniumTestCase):
    def test_successful_login_logout(self):
        """
        Verify login and logout validation, like test_web.py test, but including visual testing assertions
        """
        user = {'username': 'tomsmith', 'password': 'SuperSecretPassword!'}
        expected_login_message = "You logged into a secure area!"
        expected_logout_message = "You logged out of the secure area!"

        # Open login form
        login_page = LoginPageObject().open()
        self.assert_full_screenshot('login_form')

        # Login and check welcome message
        secure_area = login_page.login(user)
        assert_in(expected_login_message, secure_area.message.get_message())
        self.assert_full_screenshot('login_secure_area')

        # Logout and check logout message
        login_page = secure_area.logout()
        assert_in(expected_logout_message, login_page.message.get_message())
        self.assert_full_screenshot('login_logout')

    def test_successful_login_logout_visualtesting_examples(self):
        """
        This is not a logical test, it is only for showing how the visual assertions could be done.
        Verify login and logout validation, including examples of visual testing assertions
        """
        user = {'username': 'tomsmith', 'password': 'SuperSecretPassword!'}
        expected_login_message = "You logged into a secure area!"
        expected_logout_message = "You logged out of the secure area!"

        # Open login form
        login_page = LoginPageObject().open()

        # Assert the full screen
        self.assert_full_screenshot('login_form')
        # Assert the full screen excluding a web element
        self.assert_full_screenshot('login_form_no_password', exclude_elements=[login_page.password])
        # Assert the full screen excluding a web element, nonexistent excluded elements are ignored
        self.assert_full_screenshot('login_form_no_password', exclude_elements=[login_page.password, (By.ID, 'asdad')])
        # Assert only a web element
        self.assert_screenshot(login_page.login_button, 'login_submit_button')
        # Assert only a web element, directly from element
        login_page.login_button.assert_screenshot('login_submit_button')

        # Assert the full screen with a non-related baseline, it will generate an error in visual testing report
        self.assert_full_screenshot('login_form_no_password')
        # Assert a web element with a different size baseline image, it will generate an error in visual testing report
        self.assert_screenshot(login_page.login_button, 'login_form')

        # Login and check welcome message
        secure_area = login_page.login(user)
        assert_in(expected_login_message, secure_area.message.get_message())

        # Assert the full screen
        self.assert_full_screenshot('login_secure_area')
        # Assert the full screen, even if '[VisualTesting] fail' property is false
        self.assert_full_screenshot('login_secure_area', force=True)

        # Logout and check logout message
        login_page = secure_area.logout()
        assert_in(expected_logout_message, login_page.message.get_message())

        # Assert the full screen
        self.assert_full_screenshot('login_logout')
