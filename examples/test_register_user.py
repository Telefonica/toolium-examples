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
from selenium_python.pageobjects.register import RegisterPageObject
from selenium_python.pageobjects.register_result import RegisterResultPageObject


class RegisterUser(SeleniumTestCase):
    @jira('QAGROUP-1141')
    def test_successfull_register(self):
        registerPage = RegisterPageObject()
        registerPage.username = "user1"
        registerPage.password = "pass1"
        registerPage.name = "name1"
        registerPage.email = "user1@mailinator.com"
        registerPage.place = "Barcelona"
        self.logger.debug("Registering a new user")
        registerPage.submit()

        expectedMessage = "The user has been registered"
        resultPage = RegisterResultPageObject()
        self.assertIn(expectedMessage, resultPage.message)
