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

from behave import given, when, then

from toolium.driver_wrapper import DriverWrapper
from web_behave.pageobjects.login import LoginPageObject


@given('the home page is open in {browser}')
def step_impl(context, browser):
    if browser == 'browser1':
        # Use default driver
        context.current_page = {'browser1': LoginPageObject()}
    else:
        # Create a second driver
        second_wrapper = DriverWrapper()
        second_wrapper.connect()
        context.current_page['browser2'] = LoginPageObject(second_wrapper)
    # Open home page
    context.current_page[browser].open()


@when('the user logs in with username "{username}" and password "{password}" in {browser}')
def step_impl(context, username, password, browser):
    user = {'username': username, 'password': password}
    context.current_page[browser] = context.current_page[browser].login(user)


@then('the message "{message}" is shown in {browser}')
def step_impl(context, message, browser):
    assert message in context.current_page[browser].message.get_message()
