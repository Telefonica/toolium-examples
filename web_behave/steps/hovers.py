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

from behave import given, when, then

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


@given('the hovers page is open')
def step_impl(context):
    context.driver.get('{}/hovers'.format(context.toolium_config.get('Test', 'url')))


@when('the user moves mouse over the second image')
def step_impl(context):
    image2 = context.driver.find_element(By.XPATH, "//div[@class='figure'][2]/img")
    ActionChains(context.driver).move_to_element(image2).perform()


@then('the second image text shows "{expected_message}"')
def step_impl(context, expected_message):
    caption2 = context.driver.find_element(By.XPATH, "//div[@class='figure'][2]/div[@class='figcaption']/h5")
    assert caption2.text == expected_message
