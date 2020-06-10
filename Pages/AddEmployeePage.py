from Utils.Locators import Locators


class AddEmployeePage:

    def __init__(self, driver):
        self.driver = driver

        self.firstn_id = Locators.firstname_textbox
        self.lastn_id = Locators.lastname_textbox
        self.savebtn_id = Locators.savebutton

    def enter_firstname(self, first_name):
        self.driver.find_element_by_id(self.firstn_id).send_keys(first_name)

    def enter_lastname(self, last_name):
        self.driver.find_element_by_id(self.lastn_id).send_keys(last_name)

    def click_Save(self):
        self.driver.find_element_by_id(self.savebtn_id).click()
