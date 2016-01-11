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

from ddt import ddt, data, file_data
from nose.tools import assert_in

from toolium_examples.pageobjects.web.login import LoginPageObject
from toolium_examples.test_cases import SeleniumTestCase

users_dict = (
    {'username': 'peter', 'password': 'pass', 'expected_message': 'Your username is invalid!'},
    {'username': 'tomsmith', 'password': 'pass', 'expected_message': 'Your password is invalid!'},
)


@ddt
class Login(SeleniumTestCase):
    def common_wrong_login(self, user):
        """ Try to login and check error message

        :param user: dict with username, password and expected message
        """
        login_page = LoginPageObject().open()
        login_page.login(user)
        assert_in(user['expected_message'], login_page.message.get_message())

    @data(*users_dict)
    def test_wrong_login_dict(self, user):
        self.common_wrong_login(user)

    @file_data('datadriven_users.json')
    def test_wrong_login_file(self, user):
        self.common_wrong_login(user)
