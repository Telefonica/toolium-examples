# -*- coding: utf-8 -*-
'''
(c) Copyright 2014 Telefonica, I+D. Printed in Spain (Europe). All Rights
Reserved.

The copyright to the software program(s) is property of Telefonica I+D.
The program(s) may be used and or copied only with the express written
consent of Telefonica I+D or in accordance with the terms and conditions
stipulated in the agreement/contract under which the program(s) have
been supplied.
'''
from seleniumtid.selenium_test_case import SeleniumTestCase
from seleniumtid.jira import jira
from selenium_python.pageobjects.register import RegisterPageObject
from selenium_python.pageobjects.register_result import RegisterResultPageObject


class RegisterUser(SeleniumTestCase):
    @jira('QAGROUP-1141')
    def test_successfull_register(self):
        user = {'username': 'user1', 'password': 'pass1', 'name': 'name1', 'email': 'user1@mailinator.com',
                'place': 'Barcelona'}

        register_page = RegisterPageObject()
        register_page.open()
        register_page.register(user)

        result_page = RegisterResultPageObject()
        expected_message = "The user has been registered"
        self.assertIn(expected_message, result_page.message.text)
