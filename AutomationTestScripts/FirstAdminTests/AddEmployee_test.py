import time

import pytest

from Pages.HomePage import HomePage
from Pages.AddEmployeePage import AddEmployeePage
from Pages.EmployeeDetailsPage import EmployeeDetailsPage
from Utils.BaseClass import BaseClass
from Utils.CommonFunctions import CommonFunctions
from Utils import Utility as util
import moment
import allure


class TestAddEmployee(BaseClass):

    # @pytest.mark.smoke
    # def test_add_employee(self, driver):
    def test_add_employee(self):
        driver = self.driver
        log = self.getLogger()
        callfunc = CommonFunctions(driver)
        homepage = HomePage(driver)
        addEmployee = AddEmployeePage(driver)
        employeedetails = EmployeeDetailsPage(driver)

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

                header = employeedetails.verify_personal_header()
                if header:
                    log.info("New Employee created successfully")
                    assert True
                else:
                    log.info("New Employee not created successfully")
                    assert False

                self.upload_employee_docs()

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

    # @pytest.mark.depends(on=['test_add_employee'])
    def upload_employee_docs(self):
        driver = self.driver
        log = self.getLogger()
        employeedet = EmployeeDetailsPage(driver)

        try:
            employeedet.upload_docs("Mack","CXU","2013")

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

