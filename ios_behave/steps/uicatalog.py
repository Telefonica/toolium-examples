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

from ios_behave.pageobjects.uicatalog import UICatalogHome, UIAlertsView


@given('the UICatalog page is opened')
def step_impl(context):
    context.current_page = UICatalogHome()


@when('navigates to the Alerts view page')
def step_impl(context):
    context.current_page.alerts_view.click()
    context.current_page = UIAlertsView()


@when('clicks on the simple alert option')
def step_impl(context):
    context.current_page.simple.click()


@then('the alert is displayed')
def step_impl(context):
    assert context.current_page.alert.is_visible(), "Alert is not displayed"
