# -*- coding: utf-8 -*-
u"""
Copyright 2024 Telefónica Innovación Digital, S.L.
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
from web_playwright_behave.pageobjects.login import LoginPageObject


@given('the login page is open')
@async_run_until_complete
async def open_page(context):
    context.current_page = LoginPageObject()
    await context.current_page.open()


@when('the user logs in with username "{username}" and password "{password}"')
@async_run_until_complete
async def user_logs_in(context, username, password):
    user = {'username': username, 'password': password}
    context.current_page = await context.current_page.login(user)


@when('the user logs out')
@async_run_until_complete
async def user_logs_out(context):
    context.current_page = await context.current_page.logout()


@then('the message "{expected_message}" is shown')
@async_run_until_complete
async def check_message(context, expected_message):
    message = await context.current_page.message.get_message()
    assert expected_message in message, f'Expected message "{expected_message}" not found in message field: {message}'
