import time
from Utils.Locators import Locators


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.username_id = Locators.username
        self.password_id = Locators.password
        self.loginButton_id = Locators.loginButton

    def navigate_to_app_URL(self, url):
        self.driver.get(url)
        time.sleep(15)

    def enter_user_credentials(self, username, password):
        self.driver.find_element_by_id(self.username_id).send_keys(username)
        self.driver.find_element_by_id(self.password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_id(self.loginButton_id).click()
        time.sleep(20)
        welcomeText = self.driver.find_element_by_id("welcome").text
        if "Welcome" in welcomeText:
            return True
        else:
            return False
