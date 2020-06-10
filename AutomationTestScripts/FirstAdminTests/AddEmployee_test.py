import time

import pytest

from Pages.HomePage import HomePage
from Pages.AddEmployeePage import AddEmployeePage
from Utils.BaseClass import BaseClass
from Utils.CommonFunctions import CommonFunctions
from Utils import Utility as util
import moment
import allure


class TestAddEmployee(BaseClass):

    @pytest.mark.smoke
    def test_add_employee(self, driver):
        self.driver = driver
        log = self.getLogger()
        callfunc = CommonFunctions(self.driver)
        homepage = HomePage(self.driver)
        addEmployee = AddEmployeePage(self.driver)

        try:
            # Logging with Admin credentials
            loggedIn = callfunc.login_user(util.ADMIN_USERNAME, util.ADMIN_PASSWORD)

            if loggedIn:
                log.info("User logged in")
                homepage.click_PIM()
                log.info("Clicked PIM")
                homepage.click_addEmployeeLink()
                log.info("Clicked Add Employee")

                time.sleep(10)

                addEmployee.enter_firstname(util.FIRSTNAME)
                addEmployee.enter_lastname(util.LASTNAME)
                addEmployee.click_Save()

                time.sleep(10)

                url = self.driver.current_url
                if "viewPersonalDetails" in url:
                    log.info("New Employee created")
                else:
                    log.info("New Employee not created")

            else:
                log.info("User not logged in")

        except AssertionError as error:
            print("Assertion error occurred")
            print(error)
            curr_time = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
            screenshot_name = "screenshot_" + curr_time

            # To get Function name
            # test_name = util.func_name()

            allure.attach(self.driver.get_screenshot_as_png(), name=screenshot_name,
                          attachment_type=allure.attachment_type.PNG)
            self.driver.get_screenshot_as_file(
                "C:/KBData/PyCharmProjects/PythonSeleniumFrame/Screenshots/" + screenshot_name + ".png")
            raise

        except:
            print("There is an exception")
            curr_time = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
            screenshot_name = "screenshot_" + curr_time

            # To get Function name
            # test_name = util.func_name()

            allure.attach(self.driver.get_screenshot_as_png(), name=screenshot_name,
                          attachment_type=allure.attachment_type.PNG)
            self.driver.get_screenshot_as_file(
                "C:/KBData/PyCharmProjects/PythonSeleniumFrame/Screenshots/" + screenshot_name + ".png")
            raise
