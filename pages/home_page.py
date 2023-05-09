from pages.base_page import BasePage
from locators.home_page_locators import HomePageLocators


class HomePage(BasePage):
    def open(self):
        self.driver.get(self.URL)

    def get_logo(self):
        return self.driver.find_element(*HomePageLocators.LOGO).is_displayed()

