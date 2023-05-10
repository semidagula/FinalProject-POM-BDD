from behave import given, when, then
from pages.login_page import LoginPage


@given('the user is on the login page')
def step_impl(context):
    context.page = LoginPage(context.driver)
    context.page.navigate_to_website()
    context.page.go_to_logare_page()


@when('the user enters their email {email}')
def step_impl(context, email):
    context.page.enter_email(email)


@when('the user enters their password {password}')
def step_impl(context, password):
    context.page.enter_password(password)


@when('the user clicks the login button')
def step_impl(context):
    context.page.submit()


@then('the user should see an error message: {error_message}')
def step_impl(context):
    assert context.page.get_succes_message() == "PERSONAL CENTER MENU"


@then('the user should see an email error message {email_error_message}')
def step_impl(context, error_message):
    assert context.page.get_email_error_message() == error_message
