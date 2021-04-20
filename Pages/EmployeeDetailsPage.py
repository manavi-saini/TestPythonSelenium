import time
from Utils.Locators import Locators


class EmployeeDetailsPage:

    def __init__(self, driver):
        self.driver = driver
        self.personal_details = Locators.personal_details_header
        self.add_attachment_button = Locators.add_attachment
        self.upload_file = Locators.upload_file_input
        self.save_upload = Locators.save_upload

    def verify_personal_header(self):
        headerText = self.driver.find_element_by_xpath(self.personal_details).text
        if 'Personal Details' in headerText:
            return True
        else:
            return False

    def upload_docs(self, make, model, year):
        self.driver.find_element_by_id(self.add_attachment_button).click()
        filename = "VIN Upload_"+make+"_"+model+"_"+year+".csv"
        self.driver.find_element_by_id(self.upload_file).send_keys("C:/Users/sainim/Documents/PersonalTrack/CSV Files/"+filename)
        time.sleep(3)
        self.driver.find_element_by_id(self.save_upload).click()

