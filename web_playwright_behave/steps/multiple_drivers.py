# -*- coding: utf-8 -*-
u"""
Copyright 2025 Telefónica Innovación Digital, S.L.
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

from behave import given, when, then  # pylint: disable=E0611
from behave.api.async_step import async_run_until_complete
from toolium.driver_wrapper import DriverWrapper
from web_playwright_behave.pageobjects.login import LoginPageObject


@given('the login page is open in {browser}')
@async_run_until_complete
async def open_page(context, browser):
    if browser == 'browser1':
        # Use default driver
        context.current_page = {'browser1': LoginPageObject()}
    else:
        # Create a second driver
        second_wrapper = DriverWrapper()
        await second_wrapper.connect_playwright_new_page()
        context.current_page['browser2'] = LoginPageObject(second_wrapper)
    # Open home page
    await context.current_page[browser].open()


@when('the user logs in with username "{username}" and password "{password}" in {browser}')
@async_run_until_complete
async def user_logs_in(context, username, password, browser):
    user = {'username': username, 'password': password}
    context.current_page[browser] = await context.current_page[browser].login(user)


@then('the message "{expected_message}" is shown in {browser}')
@async_run_until_complete
async def check_message(context, expected_message, browser):
    message = await context.current_page[browser].message.get_message()
    assert expected_message in message, f'Expected message "{expected_message}" not found in message field: {message}'
