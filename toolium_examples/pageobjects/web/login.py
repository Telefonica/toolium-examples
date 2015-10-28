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

from toolium.pageobjects.page_object import PageObject
from toolium.pageelements import *
from message import MessagePageObject
import secure_area


class LoginPageObject(PageObject):
    username = InputText(By.ID, 'username')
    password = InputText(By.ID, 'password')
    login_button = Button(By.XPATH, "//form[@id='login']/button")
    message = MessagePageObject()

    def open(self):
        """ Open login url in browser

        :returns: page object instance
        """
        self.driver.get(self.config.get('Common', 'url'))
        return self

    def login(self, user):
        """ Fill login form and submit it

        :param user: dict with username and password values
        :returns: secure area page object instance
        """
        self.logger.debug("Login with user '{}'".format(user['username']))
        self.username.text = user['username']
        self.password.text = user['password']
        self.login_button.click()
        return secure_area.SecureAreaPageObject(self.driver)
