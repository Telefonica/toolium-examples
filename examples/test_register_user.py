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
from selenium_tid_python.selenium_test_case import SeleniumTestCase
from selenium_tid_python.jira import jira
from examples.pageobjects.register import RegisterPageObject
from examples.pageobjects.register_result import RegisterResultPageObject


class RegisterUser(SeleniumTestCase):
    @jira('QAGROUP-1141')
    def test_successfull_register(self):
        register_page = RegisterPageObject()
        register_page.username = "user1"
        register_page.password = "pass1"
        register_page.name = "name1"
        register_page.email = "user1@mailinator.com"
        register_page.place = "Barcelona"
        self.logger.debug("Registering a new user")
        register_page.submit()

        expected_message = "The user has been registered"
        result_page = RegisterResultPageObject()
        self.assertIn(expected_message, result_page.message)
