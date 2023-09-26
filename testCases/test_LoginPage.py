import pytest
from pageObjects.LoginPageObjects import Login
from Utilities.readProperties import Readconfig
from Utilities.customlogger import LoGen


class Tests_01_login:
    test_site_URL = Readconfig.GetApplicationURL()
    useremail = Readconfig.ApplicationEmail()
    password = Readconfig.Applicationpassword()

    # to run the test use:  pytest -v -s testCases/test_DDT_LoginPage.py --browser chrome to run and also generate
    # the html report use: pytest -v -s --html=Reports\reports.html testCases/test_LoginPage.py --browser chrome
    logger = LoGen.logen()


    def test_Home_title(self, setup):
        self.logger.info("*********** TEST START ***********")
        self.logger.info("************ TEST FOR THE HOME PAGE TITLE FOR THE LOGIN PAGE *************")
        self.driver = setup
        self.driver.get(self.test_site_URL)
        self.logger.info("********** OPENING THE URL AND MAXIMIZING THE WINDOW **********")
        self.driver.maximize_window()
        act_title = self.driver.title
        if act_title == "Your store. Login":
            self.logger.info("*********** HOME TITLE TEST PASSED ************")
            self.driver.close()
            assert True
        else:
            self.logger2.info("************** HOME TITLE TEST FAILED *************")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            assert False

    def test_login_flow(self, setup):
        self.logger.info("************** TEST START **************")
        self.logger.info("*********** TEST FOR THE PAGE TITLE AFTER SUCCESSFUL LOGIN ***********")
        self.driver = setup
        self.driver.get(self.test_site_URL)
        self.logger.info("************** OPENED THE URL AND MAXIMIZING THE WINDOW ***************")
        self.driver.maximize_window()
        self.lp = Login(self.driver)
        self.lp.setUserEmail(self.useremail)
        self.lp.setUserPassword(self.password)
        self.logger.info("************ INPUT OF THE CREDENTIALS INTO TEXTBOX SUCCESSFUL ************")
        self.lp.ClickSubmit()
        self.logger.info("************* CLICKING OF THE SUBMIT BUTTON ************")
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            self.logger.info("*********** LOGIN FLOW TEST PASSED ***********")
            self.driver.close()
            assert True
        else:
            self.logger2.info("********** LOGIN FLOW TEST FAILED ***********")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login_flow.png")
            self.driver.close()
            assert False
