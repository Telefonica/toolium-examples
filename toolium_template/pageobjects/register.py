# -*- coding: utf-8 -*-

u"""
(c) Copyright 2014 Telefónica, I+D. Printed in Spain (Europe). All Rights
Reserved.

The copyright to the software program(s) is property of Telefónica I+D.
The program(s) may be used and or copied only with the express written
consent of Telefónica I+D or in accordance with the terms and conditions
stipulated in the agreement/contract under which the program(s) have
been supplied.
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
