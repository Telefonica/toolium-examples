# -*- coding: utf-8 -*-
'''
(c) Copyright 2014 Telefonica, I+D. Printed in Spain (Europe). All Rights
Reserved.

The copyright to the software program(s) is property of Telefonica I+D.
The program(s) may be used and or copied only with the express written
consent of Telefonica I+D or in accordance with the terms and conditions
stipulated in the agreement/contract under which the program(s) have
been supplied.
'''
from lettuce import step, world
from examples.pageobjects.register import RegisterPageObject
from examples.pageobjects.register_result import RegisterResultPageObject
from nose.tools import assert_in
'''
Uncomment unittest2 and lettuce dependencies in requeriments.txt
and install them with pip install -r requirements.txt
'''


@step('I go to the registration form')
def open_registration_form(step):
    world.register_page = RegisterPageObject()
    world.register_page.open()


@step('I fill in field "(.*?)" with "(.*?)"')
def fill_in_field(step, field_name, value):
    field = getattr(world.register_page, field_name)
    field.text = value


@step('I select "(.*?)" from "(.*?)"')
def select_from(step, value, field_name):
    field = getattr(world.register_page, field_name)
    field.option = value


@step('I submit the registration form')
def submit_registration_form(step):
    world.logger.debug('Registering a new user')
    world.register_page.submit.element().click()


@step('I should see "(.*?)"')
def check_number(step, expected):
    result_page = RegisterResultPageObject()
    assert_in(expected, result_page.message.text)
