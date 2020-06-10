from Pages.LoginPage import LoginPage
from Utils import Utility as util
import time
import moment
import allure


class CommonFunctions:

    def __init__(self, driver):
        self.driver = driver

    def login_user(self, username, password):
        login = LoginPage(self.driver)

        try:
            # Navigating to Application URL
            # self.driver.get(util.URL)
            login.navigate_to_app_URL(util.URL)
            time.sleep(10)

            # Entering User Credentials
            login.enter_user_credentials(username, password)

            # Clicking on Login Button
            text = login.click_login()
            print(text)
            return text

        except:
            print("There is an exception")
            curr_time = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
            screenshot_name = "screenshot_" + curr_time

            # To get Function name
            # test_name = util.func_name()

            # allure.attach(self.driver.get_screenshot_as_png(), name=screenshot_name,
            #               attachment_type=allure.attachment_type.PNG)
            # self.driver.get_screenshot_as_file(
            #     "C:/KBData/PyCharmProjects/SeleniumPython/Screenshots/" + screenshot_name + ".png")
            raise
