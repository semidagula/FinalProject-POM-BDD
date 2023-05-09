class BasePage:
    URL = "https://euqs.shein.com/"

    def __init__(self, driver):
        self.driver = driver

    def back(self):
        self.driver.back() # te duce inapoi pe pagina precedenta
