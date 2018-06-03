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


@given('SpecFilesExample: the home page is open')
def step_impl(context):
    context.driver.get('{}/login'.format(context.toolium_config.get('Test', 'url')))
    context.current_page = context.get_pageobject('Login')


@when('SpecFilesExample: the user logs in with username "{username}" and password "{password}"')
def step_impl(context, username, password):
    context.current_page.username_field.text = username
    context.current_page.password_field.text = password
    context.current_page.login_button.click()
    context.current_page = context.get_pageobject('SecureArea')


@when('SpecFilesExample: the user logs out')
def step_impl(context):
    context.current_page.logout_button.click()
    context.current_page = context.get_pageobject('Login')


@then('SpecFilesExample: the message "{message}" is shown')
def step_impl(context, message):
    displayed_message = context.current_page.flash_message.wait_until_visible(2).text.splitlines()[0]
    assert message in displayed_message
