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
from seleniumtid.test_cases import SeleniumTestCase
from seleniumtid import selenium_driver
from seleniumtid.jira import jira
from examples.pageobjects.register import RegisterPageObject
from examples.pageobjects.register_result import RegisterResultPageObject
from ddt import ddt, data

users = (
    {'username': 'user1', 'password': 'pass1', 'name': 'name1', 'email': 'user1@mailinator.com', 'place': 'Barcelona'},
    {'username': 'user2', 'password': 'pass2', 'name': 'name2', 'email': 'user2@mailinator.com', 'place': 'Madrid'},
)


@ddt
class RegisterUser(SeleniumTestCase):
    def setUp(self):
        # Updating properties
        config = selenium_driver.config
        config.set('Browser', 'browser', 'firefox')
        config.set('Common', 'url', 'http://qacore02.hi.inet/sites/seleniumExamples/register.html')
        super(RegisterUser, self).setUp()

    @data(*users)
    @jira('QAGROUP-1141')
    def test_successful_register(self, user):
        register_page = RegisterPageObject()
        register_page.open()
        register_page.register(user)

        result_page = RegisterResultPageObject()
        expected_message = "The user has been registered"
        self.assertIn(expected_message, result_page.message.text)
