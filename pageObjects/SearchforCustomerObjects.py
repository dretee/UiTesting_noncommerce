import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class CustomerSearch:
    customeritem_xpath = "//*[@class='nav-icon far fa-user']/ancestor::a"
    dropdowncustomer_xpath = "//a[@href='/Admin/Customer/List']"
    emailSearchbox_xpath = "//input[@id='SearchEmail']"
    firstnameSearchbox_xpath = "//input[@id='SearchFirstName']"
    lastnameSearchbox_xpath = "//input[@id='SearchLastName']"
    DOBmonthSearchbox_xpath = "//select[@id='SearchMonthOfBirth']"
    DOBdaySearchbox_xpath = "//select[@id='SearchDayOfBirth']"
    resgistrationdatefrom_xpath = "//input[@id='SearchRegistrationDateFrom']"
    resgistrationdateto_xpath = "//input[@id='SearchRegistrationDateTo']"
    companySearchbox_xpath = "//input[@id='SearchCompany']"
    activtyfromSearch_xpath = "//input[@id='SearchLastActivityFrom']"
    activtyftoSearch_xpath = "//input[@id='SearchLastActivityTo']"
    customeroleSearchbox_xpath = "//div[@class='k-widget k-multiselect k-multiselect-clearable']"
    txt_admin_xpath = "//li[contains(text(),'Administrators')]"
    txt_Forum_Moderators_xpath = "//li[contains(text(),'Forum Moderators')]"
    txt_Guests_xpath = "//li[contains(text(),'Guests')]"
    txt_Registered_xpath = "//li[contains(text(),'Registered')]"
    txt_Vendors_xpath = "//li[contains(text(),'Vendors')]"
    table_xpath = "//div[@class='dataTables_scroll']//tbody/tr/td"
    tableRows_xpath = "//div[@class='dataTables_scroll']//tbody/tr"
    tableColumns_xpath = "//div[@class='dataTables_scroll']//tbody/tr/td"
    Searchbutton_xpath = "//button[@id='search-customers']"

    def __init__(self, driver):
        self.driver = driver

    def Customerclick(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.customeritem_xpath))).click()

    def Clickdropdowncustomer(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.dropdowncustomer_xpath))).click()

    def CustomeremailSearch(self, email):
        self.driver.find_element(By.XPATH, self.emailSearchbox_xpath).send_keys(email)

    def CustomeLNameSearch(self, Lname):
        self.driver.find_element(By.XPATH, self.lastnameSearchbox_xpath).send_keys(Lname)

    def CustomeFNameSearch(self, Fname):
        self.driver.find_element(By.XPATH, self.firstnameSearchbox_xpath).send_keys(Fname)

    def CustomerDOBMSearch(self, monthno):
        month = Select(self.driver.find_element(By.XPATH, self.DOBmonthSearchbox_xpath))
        month.select_by_visible_text(monthno)

    def CustomerDOBDSearch(self, dayno):
        day = Select(self.driver.find_element(By.XPATH, self.DOBdaySearchbox_xpath))
        day.select_by_visible_text(dayno)

    def CustomerSearchbyReg_from(self, fromdate):
        self.driver.find_element(By.XPATH, self.resgistrationdatefrom_xpath).send_keys(fromdate)

    def CustomerSearchbyReg_to(self, todate):
        self.driver.find_element(By.XPATH, self.resgistrationdateto_xpath).send_keys(todate)

    def active_from(self, acfro):
        self.driver.find_element(By.XPATH, self.activtyfromSearch_xpath).send_keys(acfro)

    def active_to(self, acto):
        self.driver.find_element(By.XPATH, self.activtyftoSearch_xpath).send_keys(acto)

    def Searchby_Company(self, company):
        self.driver.find_element(By.XPATH, self.companySearchbox_xpath).send_keys(company)

    def picking_customerrole(self, option):

        self.driver.find_element(By.XPATH, self.customeritem_xpath).click()
        self.driver.find_element(By.XPATH, "//span[@title='delete']").click()

        if option == 'Administrators':
            self.listitem = self.driver.find_element(By.XPATH, self.txt_admin_xpath)
        elif option == "Forum Moderators":
            self.listitem = self.driver.find_element(By.XPATH, self.txt_Forum_Moderators_xpath)
        elif option == "Guests":
            self.listitem = self.driver.find_element(By.XPATH, self.txt_Guests_xpath)
        elif option == "Registered":
            self.listitem = self.driver.find_element(By.XPATH, self.txt_Registered_xpath)
        elif option == "Vendors":
            self.listitem = self.driver.find_element(By.XPATH, self.txt_Vendors_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH, self.txt_Guests_xpath)
            time.sleep(3)
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def table_read(self):
        self.listdata = []
        self.table_data = self.driver.find_elements(By.XPATH, self.table_xpath)
        for data in self.table_data:
            self.listdata.append(data.text)

    def getNoOfRows(self):
        return len(self.driver.find_elements(By.XPATH, self.tableRows_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_elements(By.XPATH, self.tableColumns_xpath))

    def searchCustomerByEmail(self, email):
        global table
        flag = False
        try:
            for r in range(1, self.getNoOfRows() + 1):
                table = self.driver.find_element(By.XPATH, self.table_xpath)
                emailid = table.find_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr[" + str(r) + "]/td[2]").text
                if emailid == email:
                    flag = True
                    break
            return flag
        except NoSuchElementException:
            return flag

    def searchCustomerByName(self, Name):
        global table
        flag = False
        try:
            for r in range(1, self.getNoOfRows() + 1):
                table = self.driver.find_element(By.XPATH, self.table_xpath)
                name = table.find_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr[" + str(r) + "]/td[3]").text
                if name == Name:
                    flag = True
                    break
            return flag
        except NoSuchElementException:
            return flag

    def searchCustomerByCompany(self, Company):
        global table
        flag = False
        try:
            for r in range(1, self.getNoOfRows() + 1):
                table = self.driver.find_element(By.XPATH, self.table_xpath)
                company = table.find_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr[" + str(r) + "]/td[5]").text
                if company == Company:
                    flag = True
                    break
            return flag
        except NoSuchElementException:
            return flag

    def Search_button(self):
        self.driver.find_element(By.XPATH, self.Searchbutton_xpath).click()
