from behave import given, when, then

from toolium_examples.pageobjects.web.login import LoginPageObject


@given('the home page is open')
def step_impl(context):
    context.current_page = LoginPageObject()
    context.current_page.open()


@when('the user logs in with username "{username}" and password "{password}"')
def step_impl(context, username, password):
    user = {'username': username, 'password': password}
    context.current_page = context.current_page.login(user)


@when('the user logs out')
def step_impl(context):
    context.current_page = context.current_page.logout()


@then('the message "{message}" is shown')
def step_impl(context, message):
    assert context.current_page.message.get_message() == message
