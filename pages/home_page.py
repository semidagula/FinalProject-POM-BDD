from locators.home_page_locators import HomePageLocators


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.URL = "https://shine-boutique.ro/"

    def open(self):
        self.driver.get(self.URL)

    def get_logo(self):
        return self.driver.find_element(*HomePageLocators.LOGO).text

    def logo_displayed(self):
        return self.driver.find_element(*HomePageLocators.LOGO).is_displayed()

    def get_logo_text(self):
        return self.driver.find_element(*HomePageLocators.LOGO).text == "Shine Boutique"
