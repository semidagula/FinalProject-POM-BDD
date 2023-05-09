from behave import given, when, then

from pages.home_page import HomePage


@when(u'Login Page: I am on the shein  login page')
def step_impl(context):
    print(u'STEP: When Login Page: I am on the shein  login page')
    page = HomePage(context.driver)
    assert page.get_logo()


@given(u'Go to Login page')
def step_impl(context):
    print(u'STEP: Given Go to Login page')


@when(u'I insert email "sem.gula@gmail.com"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I insert email "sem.gula@gmail.com"')


@when(u'I insert  password "1234Supersecret!"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I insert  password "1234Supersecret!"')


@when(u'I click submit')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click submit')


@then(u'I am logged into the application and I should see "{successful_message}"')
def step_impl(context):
    print(u'STEP: Then I am logged into the application and I receive a message "PERSONAL CENTER MENU"') \


@then(u'I cannot login into the application and I receive error message "error_message"')
def step_impl(context):
    raise NotImplementedError(
        u'STEP: Then I cannot login into the application and I receive error message "error_message"')
