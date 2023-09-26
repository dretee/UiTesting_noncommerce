# import vital libraries
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class AddCustomers:
    # Define locators for web elements
    customeritem_xpath = "//*[@class='nav-icon far fa-user']/ancestor::a"
    dropdowncustomer_xpath = "//a[@href='/Admin/Customer/List']"
    addnewbutton_xpath = "//a[@class='btn btn-primary']"
    menuoption_xpath = '//*[@class="fa fa-bars"]/parent::a'
    email_txtbox_xpath = "//input[@id='Email']"
    password_txtbox_xpath = "//input[@id='Password']"
    firstname_txtbox_xpath = "//input[@id='FirstName']"
    lastname_txtbox_xpath = "//input[@id='LastName']"
    Dob_txtbox_xpath = "//input[@id='DateOfBirth']"
    companyname_txtbox_xpath = "//input[@id='Company']"
    newsletter_txtbox_xpath = "//*[@id= 'SelectedNewsletterSubscriptionStoreIds']/parent::div"
    options_for_newsletter_xpath = '//select[@id="SelectedNewsletterSubscriptionStoreIds"]/option'  # this will return a list
    rdMalebutton_txtbox_ID = "Gender_Male"
    rdFemalebutton_txtbox_ID = "Gender_Female"
    customerrole_inputbox_xpath = "//*[@id= 'SelectedCustomerRoleIds']/parent::div"
    customerrole_inputbox_options_xpath = "//*[@id= 'SelectedCustomerRoleIds']/option"
    manageVendor_dropdown_xpath = "//*[@class= 'form-control valid']"
    txt_notvendor_xpath = "//*[contains(text(),'Not a vendor')]"
    txt_vendor1_xpath = "//*[contains(text(),'Vendor 1')]"
    txt_vendor2_xpath = "//*[contains(text(),'Vendor 2')]"
    savebutton_xpath = "//button[@name='save']"
    save_n_continue_xpath = "//button[@name='save-continue']"
    txt_admin_xpath = "//li[contains(text(),'Administrators')]"
    txt_Forum_Moderators_xpath = "//li[contains(text(),'Forum Moderators')]"
    txt_Guests_xpath = "//li[contains(text(),'Guests')]"
    txt_Registered_xpath = "//li[contains(text(),'Registered')]"
    txt_Vendors_xpath = "//li[contains(text(),'Vendors')]"

    def __init__(self, driver):
        self.driver = driver

    def customerclick(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.customeritem_xpath))).click()

    def clickdropdowncustomer(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.dropdowncustomer_xpath))).click()

    def addcustomer(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.addnewbutton_xpath))).click()

    def Addtext_Emailbox(self, email):
        self.driver.find_element(By.XPATH, self.email_txtbox_xpath).send_keys(email)

    def Addtext_passwordbox(self, password):
        self.driver.find_element(By.XPATH, self.password_txtbox_xpath).send_keys(password)

    def Addtext_Fnamebox(self, first_name):
        self.driver.find_element(By.XPATH, self.firstname_txtbox_xpath).send_keys(first_name)

    def Addtext_Lnamebox(self, last_name):
        self.driver.find_element(By.XPATH, self.lastname_txtbox_xpath).send_keys(last_name)

    def gender_choice(self, gender):
        if gender == "male":
            self.driver.find_element(By.ID, self.rdMalebutton_txtbox_ID).click()
        elif gender == "female":
            self.driver.find_element(By.ID, self.rdFemalebutton_txtbox_ID).click()
        else:
            self.driver.find_element(By.ID, self.rdMalebutton_txtbox_ID).click()

    def DOB(self, date_of_birth):
        self.driver.find_element(By.XPATH, self.Dob_txtbox_xpath).send_keys(date_of_birth)

    def Addtext_companynamebox(self, company_name):
        self.driver.find_element(By.XPATH, self.companyname_txtbox_xpath).send_keys(company_name)

    def pick_from_newsoptions(self, option):
        self.driver.find_element(By.XPATH, self.newsletter_txtbox_xpath).click()

        if option == 'Your store name':
            self.listitem = self.driver.find_element(By.XPATH, "//li[contains(text(),'Your store name')]")
        elif option == "Test store 2":
            self.listitem = self.driver.find_element(By.XPATH, "//li[contains(text(),'Test store 2')]")
        else:
            self.listitem = self.driver.find_element(By.XPATH, "//li[contains(text(),'Your store name')]")
            time.sleep(3)
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def picking_customerrole(self, option):
        self.driver.find_element(By.XPATH, self.customerrole_inputbox_xpath).click()

        if option == 'Administrators':
            self.listitem = self.driver.find_element(By.XPATH, self.txt_admin_xpath)
        elif option == "Forum Moderators":
            self.listitem = self.driver.find_element(By.XPATH, self.txt_Forum_Moderators_xpath)
        elif option == "Guests":
            self.driver.find_element(By.XPATH, "//span[@title='delete']").click()
            self.listitem = self.driver.find_element(By.XPATH, self.txt_Guests_xpath)
        elif option == "Registered":
            self.listitem = self.driver.find_element(By.XPATH, self.txt_Registered_xpath)
        elif option == "Vendors":
            self.listitem = self.driver.find_element(By.XPATH, self.txt_Vendors_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH, self.txt_Guests_xpath)
            time.sleep(3)
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def manageVendorInput(self, value):
        self.driver.find_element(By.XPATH, self.manageVendor_dropdown_xpath).click()

        if value == 'Not a vendor':
            self.listitem = self.driver.find_element(By.XPATH, self.txt_notvendor_xpath)
        elif value == "Vendor 1":
            self.listitem = self.driver.find_element(By.XPATH, self.txt_vendor1_xpath)
        elif value == "Vendor 2":
            self.listitem = self.driver.find_element(By.XPATH, self.txt_vendor2_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH, self.txt_notvendor_xpath)
            time.sleep(3)
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def savebuttonsClick(self):
        self.driver.find_element(By.XPATH, self.savebutton_xpath).click()

    def savecontinueClick(self):
        self.driver.find_element(By.XPATH, self.save_n_continue_xpath).click()
