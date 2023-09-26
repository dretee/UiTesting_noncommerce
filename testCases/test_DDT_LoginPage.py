import time
import pytest
from pageObjects.LoginPageObjects import Login
from Utilities.readProperties import Readconfig
from Utilities.customlogger import LoGen
from Utilities import Xcel

# to run the test use:  pytest -v -s testCases/test_DDT_LoginPage.py --browser chrome
# the html report use: pytest -v -s --html=Reports\reports.html testCases/test_DDT_LoginPage.py --browser chrome


class Tests_02_DDT_login:
    test_site_URL = "https://admin-demo.nopcommerce.com/login"
    useremail = "admin@yourstore.com"
    password = "admin"
    Path = ".\\TestData\\DDT_noncommerce.xlsx"
    logger = LoGen.logen()

    def test_login_DDT_flow(self, setup):

        # Start the test and log the information
        self.logger.info("************** TEST START **************")
        self.logger.info("*********** TEST FOR THE PAGE TITLE AFTER SUCCESSFUL LOGIN ***********")

        # Initialize the WebDriver
        self.driver = setup
        self.driver.get(self.test_site_URL)
        self.logger.info("************** OPENED THE URL AND MAXIMIZING THE WINDOW ***************")
        self.driver.maximize_window()
        self.lp = Login(self.driver)

        # Get the number of rows in the Excel sheet
        self.rows = Xcel.getRowCount(self.Path, "Sheet1")
        print(f"number of rows: {self.rows}")
        confirm_list = []
        for r in range(3, self.rows + 1):
            self.useremail = Xcel.readData(self.Path, "Sheet1", r, 1)
            self.password = Xcel.readData(self.Path, "Sheet1", r, 2)
            self.expectedValue = Xcel.readData(self.Path, "Sheet1", r, 3)
            self.lp.setUserEmail(self.useremail)
            self.lp.setUserPassword(self.password)
            self.logger.info("************ INPUT OF THE CREDENTIALS INTO TEXTBOX SUCCESSFUL ************")
            self.lp.ClickSubmit()
            act_title = self.driver.title
            displayed_title = "Dashboard / nopCommerce administration"

            if act_title == displayed_title:
                if self.expectedValue == "Pass":
                    self.lp.ClickLogout()
                    self.logger.info("*** passed *****")
                    confirm_list.append("Pass")
                elif self.expectedValue == "Fail":
                    self.lp.ClickLogout()
                    self.logger.info("*** Failed*****")
                    confirm_list.append("Fail")

            elif act_title != displayed_title:
                if self.expectedValue == "Pass":
                    self.lp.ClickLogout()
                    self.logger.info("*** failed  *****")
                    confirm_list.append("Fail")
                elif self.expectedValue == "Fail":
                    self.logger.info("*** passed *****")
                    confirm_list.append("Pass")

        if "Fail" not in confirm_list:
            self.logger.info("********** Tests_02_DDT_login Passed ********")
            print(f"this is the list of test, {confirm_list}")
            self.driver.close()
            assert True
        else:
            self.logger.info("********** Tests_02_DDT_login Failed ********")
            print(f"this is the list of test, {confirm_list}")
            self.driver.close()
            assert False

        self.logger.info("********** Tests_02_DDT_login Completed ********")
