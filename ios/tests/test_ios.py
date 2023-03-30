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

from ios.pageobjects.calc import CalcPageObject
from ios.test_cases import IosTestCase


class IosTestApp(IosTestCase):
    def test_sum(self):
        first_number = 2
        second_number = 3

        # Sum numbers
        calc = CalcPageObject()
        calc.sum(first_number, second_number)

        # Check expected result
        assert first_number + second_number == calc.get_sum_result(), "Wrong sum"
