from lettuce import step, world
from examples.pageobjects.register import RegisterPageObject
from examples.pageobjects.register_result import RegisterResultPageObject
from nose.tools import assert_in


@step('I go to the registration form')
def open_registration_form(step):
    world.register_page = RegisterPageObject()


@step('I fill in field "(.*?)" with "(.*?)"')
def fill_in_field(step, field_name, value):
    setattr(world.register_page, field_name, value)


@step('I submit the registration form')
def submit_registration_form(step):
    world.register_page.submit()


@step('I should see "(.*?)"')
def check_number(step, expected):
    result_page = RegisterResultPageObject()
    assert_in(expected, result_page.message)
