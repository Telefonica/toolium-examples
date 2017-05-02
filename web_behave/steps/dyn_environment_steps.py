# -*- coding: utf-8 -*-
u"""
Copyright 2017 Telefónica Investigación y Desarrollo, S.A.U.
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

import time

from behave import step


@step(u'wait {value} seconds')
def wait_seconds(context, value):
    time.sleep(int(value))


@step(u'the user navigates to the "{url}" url')
def the_user_navigates_to_the_url(context, url):
    print("            url: %s" % url)


@step(u'the user logs in with username and password')
def the_user_with_name_and_pass(context):
    print("            userName: root")
    print("            password: 12345")


@step(u'step with a table')
def step_with_a_table(context):
    print("            executing the \"step with a table\"...")
    if context.table is not None:
        for row in context.table:
            print("                  %s: %s" % (row["parameter"], row["value"]))


@step(u'step with another step executed dynamically')
def step_with_a_table(context):
    i = time.time()
    print("            executing the \"step with another step executed dynamically\"...")
    context.execute_steps(u'Given wait 5 seconds')
    print("            executed the \"step with another step executed dynamically\"... took %s seconds"
          % (time.time() - i))


@step(u'step with another step using table executed dynamically')
def step_with_a_table(context):
    i = time.time()
    print("            executing the \"step with another step using table executed dynamically\"...")
    context.execute_steps(u'''
        Given step with a table
          | parameter     | value   |
          | step_fields_1 | value 1 |
          | step_fields_2 | value 2 |
          | step_fields_3 | value 3 |
          | step_fields_4 | value 4 |
    ''')
    print("            executed the \"step with another step using table executed dynamically\"... took %s seconds"
          % (time.time() - i))


@step(u'the welcome message is displayed')
def welcome_message(context):
    print("            Welcome to the Dynamic Environment.....")
