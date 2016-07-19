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

from web_behave.pageobjects.login import LoginPageObject


@given('the home page is open')
def step_impl(context):
    context.current_page = LoginPageObject()
    context.current_page.open()


@when('the user logs in with username "{username}" and password "{password}"')
def step_impl(context, username, password):
    user = {'username': username, 'password': password}
    context.current_page = context.current_page.login(user)


@when('the user logs out')
def step_impl(context):
    context.current_page = context.current_page.logout()


@then('the message "{message}" is shown')
def step_impl(context, message):
    assert message in context.current_page.message.get_message()
