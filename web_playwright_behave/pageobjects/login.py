# -*- coding: utf-8 -*-
u"""
Copyright 2024 Telefónica Innovación Digital, S.L.
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

from toolium.pageelements.playwright import InputText, Button
from toolium.pageobjects.page_object import PageObject
from web_playwright_behave.pageobjects.message import MessagePageObject
from web_playwright_behave.pageobjects.secure_area import SecureAreaPageObject


class LoginPageObject(PageObject):
    def init_page_elements(self):
        self.username = InputText(By.ID, 'username')
        self.password = InputText(By.ID, 'password')
        self.login_button = Button(By.XPATH, "//form[@id='login']/button")
        self.message = MessagePageObject()

    async def open(self):
        """ Open login url in browser

        :returns: this page object instance
        """
        await self.driver.goto(f"{self.config.get('Test', 'url')}/login")

    async def login(self, user):
        """ Fill login form and submit it

        :param user: dict with username and password values
        :returns: secure area page object instance
        """
        self.logger.debug("Login with user '%s'", user['username'])
        await self.username.fill(user['username'])
        await self.password.fill(user['password'])
        await self.login_button.click()
        return SecureAreaPageObject()
