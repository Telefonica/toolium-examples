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

from web_nose2.pageobjects.login import LoginPageObject
from web_nose2.test_cases import SeleniumTestCase


class Login(SeleniumTestCase):
    def test_successful_login_logout(self):
        user = {'username': 'tomsmith', 'password': 'SuperSecretPassword!'}
        expected_login_message = "You logged into a secure area!"
        expected_logout_message = "You logged out of the secure area!"

        # Login and check welcome message
        secure_area = LoginPageObject().open().login(user)
        assert expected_login_message in secure_area.message.get_message()

        # Logout and check logout message
        login_page = secure_area.logout()
        assert expected_logout_message in login_page.message.get_message()
