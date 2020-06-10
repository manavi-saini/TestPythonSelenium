import allure
import moment
import pytest
import time
from Utils.BaseClass import BaseClass
from AutomationTestScripts.FirstAdminTests.AddEmployee_test import TestAddEmployee
from Pages.HomePage import HomePage
from Pages.AddUserPage import AddUserPage
from Utils import Utility as util


class TestNewEmployee(BaseClass):

    @pytest.mark.regression
    def test_add_user(self):
        # driver = self.drive
        log = self.getLogger()
        homePage = HomePage(self.driver)
        addUserPage = AddUserPage(self.driver)

        try:
            TestAddEmployee.test_add_employee(TestAddEmployee(), self.driver)

            time.sleep(5)

            homePage.click_Admin()
            log.info("Admin Link clicked")
            homePage.click_addUser()
            log.info("Add User link clicked")

            time.sleep(10)

            addUserPage.selectUserRole("1")
            addUserPage.enterEmployeeName(util.FIRSTNAME + " " + util.LASTNAME)
            addUserPage.enter_username(util.CEO_USERNAME)

            selected = addUserPage.verifyStatus()
            if selected == "Enabled":
                assert True
            else:
                addUserPage.selectStatus("Enabled")

            addUserPage.enter_password(util.CEO_PASSWORD)
            addUserPage.enter_confirmpassword(util.CEO_PASSWORD)
            addUserPage.click_Save()

            time.sleep(10)

            homePage.search_username(util.CEO_USERNAME)
            homePage.click_search()
            search = homePage.verifycorrectuser().text
            time.sleep(10)
            if util.CEO_USERNAME == search:
                log.info("user created successfully")
                assert True
            else:
                log.info("user not created")
                assert False

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
