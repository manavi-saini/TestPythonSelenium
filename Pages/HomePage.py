from Utils.Locators import Locators


class HomePage:

    def __init__(self, driver):
        self.driver = driver

        self.pim_module_id = Locators.pim_module_menu_link
        self.add_employee_id = Locators.add_employee_menu_link
        self.admin_id = Locators.admin_menu_link
        self.adduser_id = Locators.adduser_button
        self.username_id = Locators.username_textbox
        self.searchbutton_id = Locators.searchbutton
        self.searcheduser = Locators.searcheduser_table

    def click_PIM(self):
        self.driver.find_element_by_id(self.pim_module_id).click()

    def click_addEmployeeLink(self):
        self.driver.find_element_by_id(self.add_employee_id).click()

    def click_Admin(self):
        self.driver.find_element_by_id(self.admin_id).click()

    def click_addUser(self):
        self.driver.find_element_by_id(self.adduser_id).click()

    def search_username(self, name):
        self.driver.find_element_by_id(self.username_id).send_keys(name)

    def click_search(self):
        self.driver.find_element_by_id(self.searchbutton_id).click()

    def verifycorrectuser(self):
        searched = self.driver.find_element_by_xpath(self.searcheduser)
        return searched
