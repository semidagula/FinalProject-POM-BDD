from behave import given, when, then

from pages.home_page import HomePage


@given("User is on the Home page")
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.open()


@when("User looks at the logo")
def step_impl(context):
    context.logo_displayed = context.home_page.logo_displayed()


@when("Logo should be displayed")
def step_impl(context):
    assert context.logo_displayed is True
