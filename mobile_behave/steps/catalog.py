# -*- coding: utf-8 -*-
u"""
Copyright 2016 Telefónica Investigación y Desarrollo, S.A.U.
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

from mobile_behave.pageobjects.initial import BaseInitialPageObject


@given('OpenShop.io app is open')
def step_impl(context):
    context.current_page = BaseInitialPageObject().wait_until_loaded()


@when('the user goes to the shop')
def step_impl(context):
    context.current_page = context.current_page.go_to_shop()


@then('just arrived collections are shown')
def step_impl(context):
    assert context.current_page.title.text.upper() == 'JUST ARRIVED'
    assert len(context.current_page.get_collections()) > 1
