from behave import given, when, then

from pages.home_page import HomePage


@when(u'Login Page: I am on the shein  login page')
def step_impl(context):
    page = HomePage(context.driver)
    assert page.open()


@then(u'I should see "Shein "')
def step_impl(context):
    print(u'STEP: Then I should see "Shein "')
    page = HomePage(context.driver)
    assert page.get_logo()
