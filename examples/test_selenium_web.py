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

import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from seleniumtid.test_cases import SeleniumTestCase
from seleniumtid.jira import jira
from seleniumtid import selenium_driver
from examples.pageobjects.register import RegisterPageObject
from examples.pageobjects.register_result import RegisterResultPageObject


class RegisterUser(SeleniumTestCase):
    def setUp(self):
        root_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        os.environ['Files_properties'] = os.path.join(root_path, 'conf', 'examples', 'properties.cfg')
        os.environ['Files_logging'] = os.path.join(root_path, 'conf', 'examples', 'logging.conf')
        os.environ['Files_output_path'] = os.path.join(root_path, 'dist')
        super(RegisterUser, self).setUp()

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

    def test_successful_register_without_page_objects(self):
        user = {'username': 'user1', 'password': 'pass1', 'name': 'name1', 'email': 'user1@mailinator.com',
                'place': 'Barcelona'}

        self.driver.get(selenium_driver.config.get('Common', 'url'))

        self.logger.debug("Registering a new user")
        self.driver.find_element(By.NAME, 'username').send_keys(user['username'])
        self.password = self.driver.find_element(By.ID, 'password').send_keys(user['password'])
        self.name = self.driver.find_element(By.ID, 'name').send_keys(user['name'])
        self.email = self.driver.find_element(By.ID, 'email').send_keys(user['email'])
        Select(self.driver.find_element(By.ID, 'place')).select_by_visible_text(user['place'])
        self.driver.find_element(By.ID, 'registerButton').click()
        self.assertScreenshot('body', 'register_result')

        result_message = self.driver.find_element(By.XPATH, "//div[@id='content']/div/div/div/b[2]").text
        expected_message = "The user has been registered"
        self.assertIn(expected_message, result_message)
