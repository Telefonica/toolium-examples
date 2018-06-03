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

from web.test_cases import SeleniumTestCase


class LoginUsingSpecFiles(SeleniumTestCase):
    """
    TestCases using PageObject Specification Files
    """

    def setUp(self):
        super(LoginUsingSpecFiles, self).setUp()

        # Open URL
        self.driver.get('{}/login'.format(self.config.get('Test', 'url')))

    def test_successful_login_logout(self):
        # Login and check welcome message
        self.logger.debug("Login with user '%s'", 'tomsmith')

        current_page = self.get_pageobject('Login')
        current_page.username_field.text = 'tomsmith'
        current_page.password_field.text = 'SuperSecretPassword!'
        current_page.login_button.click()
        current_page = self.get_pageobject('SecureArea')

        message = current_page.flash_message.wait_until_visible(2).text.splitlines()[0]
        assert_in("You logged into a secure area!", message)

        # Logout and check logout message
        current_page.logout_button.click()
        current_page = self.get_pageobject('Login')

        message = current_page.flash_message.wait_until_visible(2).text.splitlines()[0]
        assert_in("You logged out of the secure area!", message)
