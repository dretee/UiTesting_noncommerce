import string
import time
import pytest
from pageObjects.LoginPageObjects import Login
from Utilities.readProperties import Readconfig
from Utilities.customlogger import LoGen
from pageObjects.addcustomerelements import AddCustomers
from selenium.webdriver.common.by import By
import random


# to run the test use:  pytest -v -s testCases/test_AddCustomer.py --browser chrome
# the html report use: pytest -v -s --html=Reports\reports.html testCases/test_AddCustomer.py --browser chrome

def randon_generator(size=8, chars=string.ascii_lowercase + string.digits):  # randon email generator
    return ''.join(random.choice(chars) for x in range(size))


class Tests_03_AddCustomer:
    test_site_URL = Readconfig.GetApplicationURL()
    useremail = Readconfig.ApplicationEmail()
    password = Readconfig.Applicationpassword()
    logger = LoGen.logen()

    def test_AddCustomer(self, setup):
        try:
            # Start the test and log the information
            self.logger.info("************** TEST START **************")
            self.logger.info("*********** TEST FOR THE PAGE TITLE AFTER SUCCESSFUL LOGIN ***********")

            # Initialize the WebDriver
            self.driver = setup
            self.driver.get(self.test_site_URL)
            self.logger.info("************** OPENED THE URL AND MAXIMIZING THE WINDOW ***************")
            self.driver.maximize_window()
            self.lp = Login(self.driver)
            self.lp.setUserEmail(self.useremail)
            self.lp.setUserPassword(self.password)
            self.logger.info("************ INPUT OF THE CREDENTIALS INTO TEXTBOX SUCCESSFUL ************")
            self.logger.info("************* CLICKING OF THE SUBMIT BUTTON ************")
            self.lp.ClickSubmit()
            time.sleep(3)
            self.logger.info("******* navigating to the add new user frame *******")
            self.ac = AddCustomers(self.driver)
            self.ac.customerclick()
            self.ac.clickdropdowncustomer()
            self.ac.addcustomer()
            self.logger.info("******* inputing data for the new user *******")
            self.email = randon_generator() + "@gmail.com"
            self.ac.Addtext_Emailbox(self.email)
            self.ac.Addtext_passwordbox("Quser")
            self.ac.Addtext_Fnamebox("Anthony")
            self.ac.Addtext_Lnamebox('Uyah')
            self.ac.gender_choice("male")
            self.ac.DOB("08/01/1996")
            self.ac.Addtext_companynamebox("google")
            self.ac.pick_from_newsoptions("Test store 2")
            self.ac.picking_customerrole('Vendors')
            # self.ac.manageVendorInput("Vendor 1")
            time.sleep(10)
            self.ac.savebuttonsClick()
            self.logger.info("***** The Form Has Been Filled completely *******")

            self.bodytxt = self.driver.find_element(By.TAG_NAME, "body").text

            if "customer has been added successfully" in self.bodytxt:
                self.logger.info("****** The Add Customer Test Passed *******")
                assert True

        except Exception as e:
            # Handle exceptions and log error messages
            self.logger.error(f"Error occurred: {str(e)}")
            self.logger.info("******** The Add Customer Test Failed ********")
            assert False
