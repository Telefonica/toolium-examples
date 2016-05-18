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
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from toolium_examples.test_cases import IosTestCase


class IosTestApp(IosTestCase):
    def test_sum(self):
        first_number = 2
        second_number = 3

        # Input numbers and click button
        first_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//UIATextField[1]")))
        first_element.send_keys(first_number)
        self.driver.find_element_by_xpath("//UIATextField[2]").send_keys(second_number)
        self.driver.find_element_by_accessibility_id("ComputeSumButton").click()

        # Check expected result
        result = int(self.driver.find_element_by_xpath("//UIAStaticText[1]").text)
        assert_equal(first_number + second_number, result, "Wrong sum")
