import pytest
import allure
import moment

from Utils.BaseClass import BaseClass
from Utils.CommonFunctions import CommonFunctions
from Utils import Utility as util


class TestLogin(BaseClass):

    @pytest.mark.regression
    @pytest.mark.smoke
    def test_admin_login(self):
        driver = self.driver
        log = self.getLogger()
        callfunc = CommonFunctions(driver)

        try:
            # Logging with Admin credentials
            loggedIn = callfunc.login_user(util.ADMIN_USERNAME, util.ADMIN_PASSWORD)

            if loggedIn:
                log.info("User logged in successfully")
            else:
                log.info("User not logged in successfully")

        except AssertionError as error:
            print("Assertion error occurred")
            print(error)
            curr_time = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
            screenshot_name = "screenshot_" + curr_time

            # To get Function name
            # test_name = util.func_name()

            allure.attach(self.driver.get_screenshot_as_png(), name=screenshot_name,
                          attachment_type=allure.attachment_type.PNG)
            driver.get_screenshot_as_file(
                "C:/KBData/PyCharmProjects/SeleniumPython/Screenshots/" + screenshot_name + ".png")
            raise

        except:
            print("There is an exception")
            curr_time = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
            screenshot_name = "screenshot_" + curr_time

            # To get Function name
            # test_name = util.func_name()

            allure.attach(self.driver.get_screenshot_as_png(), name=screenshot_name,
                          attachment_type=allure.attachment_type.PNG)
            driver.get_screenshot_as_file(
                "C:/KBData/PyCharmProjects/SeleniumPython/Screenshots/" + screenshot_name + ".png")
            raise

        else:
            print("No exceptions occurred")

        finally:
            print("This block will always execute. Finally block")

    # @pytest.mark.regression
    # def test_ceo_login(self):
    #     driver = self.driver
    #     log = self.getLogger()
    #     callfunc = CommonFunctions(driver)
    #
    #     try:
    #         # Logging with CEO credentials
    #         loggedIn = callfunc.login_user(util.CEO_USERNAME, util.CEO_PASSWORD)
    #
    #         if loggedIn:
    #             log.info("User logged in successfully")
    #         else:
    #             log.info("User not logged in successfully")
    #
    #     except AssertionError as error:
    #         print("Assertion error occurred")
    #         print(error)
    #         curr_time = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
    #         screenshot_name = "screenshot_" + curr_time
    #
    #         # To get Function name
    #         # test_name = util.func_name()
    #
    #         allure.attach(self.driver.get_screenshot_as_png(), name=screenshot_name,
    #                       attachment_type=allure.attachment_type.PNG)
    #         driver.get_screenshot_as_file(
    #             "C:/KBData/PyCharmProjects/SeleniumPython/Screenshots/" + screenshot_name + ".png")
    #         raise
    #
    #     except:
    #         print("There is an exception")
    #         curr_time = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
    #         screenshot_name = "screenshot_" + curr_time
    #
    #         # To get Function name
    #         # test_name = util.func_name()
    #
    #         allure.attach(self.driver.get_screenshot_as_png(), name=screenshot_name,
    #                       attachment_type=allure.attachment_type.PNG)
    #         driver.get_screenshot_as_file(
    #             "C:/KBData/PyCharmProjects/SeleniumPython/Screenshots/" + screenshot_name + ".png")
    #         raise

