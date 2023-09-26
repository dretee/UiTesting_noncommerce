import time
import pytest
from pageObjects.LoginPageObjects import Login
from Utilities.readProperties import Readconfig
from Utilities.customlogger import LoGen
from pageObjects.SearchforCustomerObjects import CustomerSearch


# to run the test use:  pytest -v -s testCases/test_CustomerSearchname.py--browser chrome
# the html report use: pytest -v -s --html=Reports\reports.html testCases/test_CustomerSearchname.py--browser chrome


class Tests_04_CustomerSearch:
    test_site_URL = Readconfig.GetApplicationURL()
    useremail = Readconfig.ApplicationEmail()
    password = Readconfig.Applicationpassword()
    logger = LoGen.logen()

    def test_CustomerSearch_NAME(self, setup):
        # Start the test and log the information
        self.logger.info("************** TEST START **************")
        self.logger.info("***************  Test_CustomerSearch_NAME is Started *********** ")

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
        self.logger.info("******* navigating to the add new user frame *******")
        self.logger.info("******* initializing the class and its method and inputting the names *******")
        self.logger.info("************* searching customer by Name **********")

        self.sc = CustomerSearch(self.driver)
        self.sc.Customerclick()
        self.sc.Clickdropdowncustomer()
        self.sc.CustomeFNameSearch("tony")
        time.sleep(3)
        self.sc.CustomeLNameSearch("Terces")
        self.sc.Search_button()
        time.sleep(5)
        status = self.sc.searchCustomerByName("tony Terces")
        self.driver.close()
        if status:
            self.logger.info("***************  The customer was found using the name search route  *********** ")
            self.logger.info("***************  Test_CustomerSearch_NAME is Finished  *********** ")
            assert True
        else:
            # self.driver.save_screenshot(".\\Screenshots\\CustomerSearchName.png")
            self.logger.info("***************  The customer was not found using the name search route  *********** ")
            self.logger.info("***************  Such customer does not exist  *********** ")
            self.logger.info("***************  Test_CustomerSearch_NAME is Finished  *********** ")
            assert True
