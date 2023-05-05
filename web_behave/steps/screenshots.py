# -*- coding: utf-8 -*-
u"""
Copyright 2023 Telefónica Investigación y Desarrollo, S.A.U.
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

from behave import then

from selenium.webdriver.common.by import By


@then('the full screenshot is equal to "{screenshot_name}" image')
def step_impl(context, screenshot_name):
    context.assert_full_screenshot(screenshot_name)


@then('the full screenshot is equal to "{screenshot_name}" image excluding elements')
def step_impl(context, screenshot_name):
    excluded_elements = []
    for row in context.table:
        if row['type'] == 'element':
            excluded_elements.append(
                getattr(context.current_page, row['locator']))
        else:
            excluded_elements.append(
                (getattr(By, row['type']), row['locator']))

    context.assert_full_screenshot(
        screenshot_name, exclude_elements=excluded_elements)


@then('the "{element}" element screenshot is equal to "{expected_message}" image')
def step_impl(context, element, expected_message):
    getattr(context.current_page, element).assert_screenshot(expected_message)
