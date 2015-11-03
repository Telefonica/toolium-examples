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

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from toolium_examples.test_cases import SeleniumTestCase


class Login(SeleniumTestCase):
    def test_successful_login_logout(self):
        user = {'username': 'tomsmith', 'password': 'SuperSecretPassword!'}
        expected_login_message = "You logged into a secure area!"
        expected_logout_message = "You logged out of the secure area!"

        # Open url
        self.driver.get(self.config.get('Common', 'url'))

        # Login and check welcome message
        self.driver.find_element_by_id('username').send_keys(user['username'])
        self.driver.find_element_by_id('password').send_keys(user['password'])
        self.driver.find_element_by_xpath("//form[@id='login']/button").click()
        message = self.driver.find_element_by_id('flash').text.splitlines()[0]
        self.assertIn(expected_login_message, message)

        # Logout and check logout message
        self.driver.find_element_by_xpath("//div[@id='content']//a[contains(@class,'button')]").click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'username')))
        message = self.driver.find_element_by_id('flash').text.splitlines()[0]
        self.assertIn(expected_logout_message, message)
