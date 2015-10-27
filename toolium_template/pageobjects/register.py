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


class RegisterPageObject(PageObject):
    username = InputText(By.NAME, 'username')
    password = InputText(By.ID, 'password')
    name = InputText(By.ID, 'name')
    email = InputText(By.ID, 'email')
    place = Select(By.ID, 'place')
    submit = Button(By.ID, 'registerButton')

    def open(self):
        self.driver.get(self.config.get('Common', 'url'))

    def register(self, user):
        self.logger.debug("Registering a new user")
        self.username.text = user['username']
        self.password.text = user['password']
        self.name.text = user['name']
        self.email.text = user['email']
        self.place.option = user['place']
        self.submit.click()
