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

from lettuce import step, world
from nose.tools import assert_in

from toolium_examples.pageobjects.web.login import LoginPageObject


@step('the home page is open')
def open_home_page(step):
    world.current_page = LoginPageObject()
    world.current_page.open()


@step('the user logs in with username "(.*?)" and password "(.*?)"')
def login(step, username, password):
    user = {'username': username, 'password': password}
    world.current_page = world.current_page.login(user)


@step('the user logs out')
def logout(step):
    world.current_page = world.current_page.logout()


@step('the message "(.*?)" is shown')
def step_impl(step, message):
    assert_in(message, world.current_page.message.get_message())
