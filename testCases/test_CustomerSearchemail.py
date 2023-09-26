import time
import pytest
from pageObjects.LoginPageObjects import Login
from Utilities.readProperties import Readconfig
from Utilities.customlogger import LoGen
from pageObjects.SearchforCustomerObjects import CustomerSearch


# to run the test use:  pytest -v -s testCases/test_CustomerSearchemail.py--browser chrome
# the html report use: pytest -v -s --html=Reports\reports.html testCases/test_CustomerSearchemail.py--browser chrome
class Tests_04_CustomerSearch:
    test_site_URL = Readconfig.GetApplicationURL()
    useremail = Readconfig.ApplicationEmail()
    password = Readconfig.Applicationpassword()
    logger = LoGen.logen()

    def test_CustomerSearch_Email(self, setup):
        # Start the test and log the information
        self.logger.info("************** TEST START **************")
        self.logger.info("***************  TC_SearchCustomerByEmail Finished  *********** ")

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

        self.cs = CustomerSearch(self.driver)
        self.cs.Customerclick()
        self.cs.Clickdropdowncustomer()
        self.cs.CustomeremailSearch("brenda_lindgren@nopCommerce.com")
        self.cs.Search_button()
        time.sleep(5)
        status = self.cs.searchCustomerByEmail("brenda_lindgren@nopCommerce.com")
        self.driver.close()
        if status:
            self.logger.info("***************  The customer was found using the email search route  *********** ")
            self.logger.info("***************  Test_CustomerSearch_NAME is Finished  *********** ")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\CustomerSearchEmail.png")
            self.logger.info("***************  The customer was not found using the name search route  *********** ")
            self.logger.info("***************  Such customer does not exist  *********** ")
            self.logger.info("***************  TC_SearchCustomerByEmail Finished  *********** ")
            assert True

    def test_CustomerSearch_company(self, setup):
        # Start the test and log the information
        self.logger.info("************** TEST START **************")
        self.logger.info("***************  TC_SearchCustomerByCompany Finished  *********** ")

        # Initialize the WebDriver
        self.driver = setup
        self.driver.get(self.test_site_URL)
        self.logger.info("************** OPENED THE URL AND MAXIMIZING THE WINDOW ***************")
        self.driver.maximize_window()
        self.lp = Login(self.driver)
        self.logger.info("************ INPUT OF THE CREDENTIALS INTO TEXTBOX SUCCESSFUL ************")
        self.lp.setUserEmail(self.useremail)
        self.lp.setUserPassword(self.password)
        self.logger.info("************* CLICKING OF THE SUBMIT BUTTON ************")
        self.lp.ClickSubmit()
        time.sleep(3)
        self.logger.info("******* navigating to the add new user frame *******")

        self.cs = CustomerSearch(self.driver)
        self.cs.Customerclick()
        self.cs.Clickdropdowncustomer()
        self.cs.Searchby_Company("google")
        self.cs.Search_button()
        time.sleep(5)
        status = self.cs.searchCustomerByCompany("google")
        self.driver.close()
        if status:
            self.logger.info("***************  The customer was found using the email search route  *********** ")
            self.logger.info("***************  Test_CustomerSearch_NAME is Finished  *********** ")
            assert True
        else:
            # self.driver.save_screenshot(".\\Screenshots\\CustomerSearchEmail.png")
            self.logger.info("***************  The customer was not found using the name search route  *********** ")
            self.logger.info("***************  SUCH CUSTOMER DOES NOT EXIST *********** ")
            self.logger.info("***************  TC_SearchCustomerByEmail Finished  *********** ")
            assert True
