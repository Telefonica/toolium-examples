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

from toolium.jira import jira

from toolium_template.test_cases import SeleniumTestCase
from toolium_template.pageobjects.register import RegisterPageObject
from toolium_template.pageobjects.register_result import RegisterResultPageObject


class RegisterUser(SeleniumTestCase):
    @jira('QAGROUP-1141')
    def test_successful_register(self):
        user = {'username': 'user1', 'password': 'pass1', 'name': 'name1', 'email': 'user1@mailinator.com',
                'place': 'Barcelona'}

        register_page = RegisterPageObject()
        register_page.open()
        register_page.register(user)
        self.assertScreenshot('body', 'register_result')

        result_page = RegisterResultPageObject()
        expected_message = "The user has been registered"
        self.assertIn(expected_message, result_page.message.text)
