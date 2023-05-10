from selenium.webdriver.common.by import By


class LoginLocators:
    LOGIN_BUTTON = (By.XPATH, "///em[normalize-space()='Sign in / Register']")
    EMAIL = (By.XPATH, "//input[@aria-label='Email Address:']")
    PAROLA = (By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div[2]/div[1]/div[3]/div/div[3]/div[2]/div[1]/div/input')

    CONTINUE = (By.CSS_SELECTOR, "//span[normalize-space()='Sign In']")
    SKIP = (By.XPATH, "//span[normalize-space()='Skip']")

    PERSONAL_CENTER_MENU = (By.XPATH, "//h3[@title='Personal Center']")

    PASSWORD_ERROR_MESSAGE = (By.XPATH, "//div[@id='advice-validate-password-pass']")
