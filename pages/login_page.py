from locators.login_locators import LoginLocators


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.URL = "https://shine-boutique.ro/"

    def navigate_to_website(self):
        self.driver.get(self.URL)

    def go_to_logare_page(self):
        self.driver.find_element(*LoginLocators.LOGIN_BUTTON).click()

    def enter_email(self, email):
        email_field = self.driver.find_element(*LoginLocators.EMAIL)
        email_field.clear()
        email_field.send_keys(email)

    def enter_password(self, password):
        password_field = self.driver.find_element(*LoginLocators.PAROLA)
        password_field.clear()
        password_field.send_keys(password)

    def submit(self):
        self.driver.find_element(*LoginLocators.CONTINUE).click()

    def get_succes_message(self):
        return self.driver.find_element(*LoginLocators.PERSONAL_CENTER_MENU).text

    def get_email_error_message(self):
        return self.driver.find_element(*LoginLocators.PASSWORD_ERROR_MESSAGE).text
