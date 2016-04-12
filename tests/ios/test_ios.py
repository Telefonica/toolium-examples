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

from toolium_examples.pageobjects.ios.calc import CalcPageObject
from toolium_examples.test_cases import iOSTestCase


class IosTestApp(iOSTestCase):
    def test_sum(self):
        first_number = 2
        second_number = 3

        # Sum numbers
        calc = CalcPageObject()
        calc.sum(first_number, second_number)

        # Check expected result
        result = int(calc.result.text)
        self.logger.debug("{} + {} = {}".format(first_number, second_number, result))
        assert_equal(first_number + second_number, result, "Wrong sum")
