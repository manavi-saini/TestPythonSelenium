from selenium.webdriver.support.select import Select
from Utils.Locators import Locators


class AddUserPage:

    def __init__(self, driver):
        self.driver = driver

        self.userrole_id = Locators.userrole_dropdown
        self.employeename_id = Locators.employeename_textbox
        self.username_id = Locators.usrname_textbox
        self.statusdropdown_id = Locators.statusdropdown
        self.pwd_id = Locators.pwd_textbox
        self.confpwd_id = Locators.confpwd_textbox
        self.savebtn_id = Locators.savebutton

    def selectUserRole(self, value):
        roledrop = Select(self.driver.find_element_by_id(self.userrole_id))
        roledrop.select_by_value(value)

    def enterEmployeeName(self, name):
        self.driver.find_element_by_id(self.employeename_id).send_keys(name)

    def enter_username(self, username):
        self.driver.find_element_by_id(self.username_id).send_keys(username)

    def verifyStatus(self):
        statusdrop = Select(self.driver.find_element_by_id(self.statusdropdown_id))
        selected = statusdrop.first_selected_option
        return selected

    def selectStatus(self, text):
        statusdrop1 = Select(self.driver.find_element_by_id(self.statusdropdown_id))
        statusdrop1.select_by_visible_text(text)

    def enter_password(self, pwd):
        self.driver.find_element_by_id(self.pwd_id).send_keys(pwd)

    def enter_confirmpassword(self, pwd):
        self.driver.find_element_by_id(self.confpwd_id).send_keys(pwd)

    def click_Save(self):
        self.driver.find_element_by_id(self.savebtn_id).click()
