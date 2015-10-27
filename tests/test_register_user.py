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
