from selenium.webdriver.common.by import By

from locators.login_locators import LoginLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    def open(self):
        self.driver.get(self.URL)

    def go_to_logare_page(self):
        self.driver.find_element(*LoginLocators.LOGIN_BUTTON).click()

    def enter_email(self, email):
        self.driver.find_element(*LoginLocators.EMAIL).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*LoginLocators.PAROLA).send_keys(password)

    def submit(self):
        self.driver.find_element(*LoginLocators.CONTINUE).click()

    def successful_login(self):
        return self.driver.find_element(By.XPATH, "//h3[@title='Personal Center']").text
