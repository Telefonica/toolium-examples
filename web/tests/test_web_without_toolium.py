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

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Login(TestCase):
    """This is the same test as test_web.py but without using Toolium"""

    def setUp(self):
        # Create a new chrome driver before each test
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def tearDown(self):
        # Close driver and browser
        self.driver.quit()

    def test_successful_login_logout(self):
        user = {'username': 'tomsmith', 'password': 'SuperSecretPassword!'}
        expected_login_message = "You logged into a secure area!"
        expected_logout_message = "You logged out of the secure area!"

        # Open url
        self.driver.get('http://the-internet.herokuapp.com/login')

        # Login and check welcome message
        self.driver.find_element(By.ID, 'username').send_keys(user['username'])
        self.driver.find_element(By.ID, 'password').send_keys(user['password'])
        self.driver.find_element(By.XPATH, "//form[@id='login']/button").click()
        message = self.driver.find_element(By.ID, 'flash').text.splitlines()[0]
        assert expected_login_message in message

        # Logout and check logout message
        self.driver.find_element(By.XPATH, "//div[@id='content']//a[contains(@class,'button')]").click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'username')))
        message = self.driver.find_element(By.ID, 'flash').text.splitlines()[0]
        assert expected_logout_message in message
