"""
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

from behave import then, when
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@when('the user opens a new tab')
def user_opens_new_tab(context):
    # Open a new tab (Ctrl+t)
    ActionChains(context.driver).key_down(Keys.CONTROL).send_keys('t').key_up(Keys.CONTROL).perform()


@when('the user closes the tab')
def user_closes_tab(context):
    # Close tab (Ctrl+F4)
    ActionChains(context.driver).key_down(Keys.CONTROL).send_keys(Keys.F4).key_up(Keys.CONTROL).perform()


@then('the username field is visible')
def username_field_is_visible(context):
    # Check that an element of the first tab is visible
    context.driver.find_element(By.ID, 'username')
