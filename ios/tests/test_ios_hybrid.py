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

from nose.tools import assert_equal
from selenium.webdriver.common.by import By

from ios.test_cases import IosHybridTestCase


class IosHybrid(IosHybridTestCase):
    def test_search_employees(self):
        search_letter = 'j'
        expected_employees = 5

        # Switch to webview context
        self.utils.switch_to_first_webview_context()

        # Search employees that starts with selected letter
        input_text = self.utils.wait_until_element_visible((By.TAG_NAME, 'input'))
        input_text.send_keys(search_letter)

        # Count employees
        employees = self.driver.find_elements(By.TAG_NAME, 'li')
        assert_equal(expected_employees, len(employees), 'Wrong number of employees')
