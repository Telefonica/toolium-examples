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

from toolium.pageelements.playwright import Button
from toolium.pageobjects.page_object import PageObject
from web_playwright_behave.pageobjects.message import MessagePageObject


class SecureAreaPageObject(PageObject):
    def init_page_elements(self):
        self.message = MessagePageObject()
        self.logout_button = Button(By.XPATH, "//div[@id='content']//a[contains(@class,'button')]")

    async def logout(self):
        """ Log out of secure area

        :returns: login page object instance
        """
        from web_playwright_behave.pageobjects.login import LoginPageObject  # pylint: disable=C0415

        await self.logout_button.click()
        return LoginPageObject()
