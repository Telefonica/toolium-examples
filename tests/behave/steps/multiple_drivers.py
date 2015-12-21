from behave import given, when, then

from toolium.driver_wrapper import DriverWrapper
from toolium_examples.pageobjects.web.login import LoginPageObject


@given('the home page is open in {browser}')
def step_impl(context, browser):
    if browser == 'browser1':
        # Use default driver
        context.current_page = {'browser1': LoginPageObject()}
    else:
        # Create a second driver
        second_wrapper = DriverWrapper()
        second_wrapper.connect()
        context.current_page['browser2'] = LoginPageObject(second_wrapper)
    # Open home page
    context.current_page[browser].open()


@when('the user logs in with username "{username}" and password "{password}" in {browser}')
def step_impl(context, username, password, browser):
    user = {'username': username, 'password': password}
    context.current_page[browser] = context.current_page[browser].login(user)


@then('the message "{message}" is shown in {browser}')
def step_impl(context, message, browser):
    assert context.current_page[browser].message.get_message() == message
