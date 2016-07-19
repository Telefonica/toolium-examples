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

from ios_behave.pageobjects.calc import CalcPageObject


@given('the calculator is open')
def step_impl(context):
    context.current_page = CalcPageObject()


@when('the user adds {first_number} and {second_number}')
def step_impl(context, first_number, second_number):
    context.current_page.sum(first_number, second_number)


@then('the result is {expected_result}')
def step_impl(context, expected_result):
    assert int(expected_result) == context.current_page.get_sum_result()
