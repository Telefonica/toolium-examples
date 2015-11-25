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

from selenium.webdriver.common.by import By

from toolium_examples.pageobjects.web.login import LoginPageObject
from toolium_examples.test_cases import iOSWebTestCase


class iOSWeb(iOSWebTestCase):
    def test_successful_login_logout(self):
        user = {'username': 'tomsmith', 'password': 'SuperSecretPassword!'}
        expected_login_message = "You logged into a secure area!"
        expected_logout_message = "You logged out of the secure area!"

        # Login and check welcome message
        secure_area = LoginPageObject().open().login(user)
        self.assertIn(expected_login_message, secure_area.message.get_message())

        # Logout and check logout message
        login_page = secure_area.logout()
        self.assertIn(expected_logout_message, login_page.message.get_message())

    def test_swipe_ios8(self):
        self.driver.get('http://the-internet.herokuapp.com/infinite_scroll')
        scroll_elem = self.driver.find_element(By.XPATH, "//*[@class='jscroll-inner']")
        self.driver.switch_to.context('NATIVE_APP')
        # Javascript exception in ios 8
        self.driver.execute_script("mobile: scroll", {"direction": "down", "element": scroll_elem.getAttribute("id")})
        self.driver.switch_to.context('WEBVIEW')

    def test_swipe_ios9(self):
        self.driver.get('http://the-internet.herokuapp.com/infinite_scroll')
        self.driver.switch_to.context('NATIVE_APP')
        self.driver.swipe(50, 400, 50, 200, 500)
        self.driver.switch_to.context('WEBVIEW')
