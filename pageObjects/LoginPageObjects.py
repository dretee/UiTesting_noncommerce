import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login:
    Email_textbox_by_xpath = "//input[@id='Email']"
    Password_textbox_by_id = "Password"
    Login_button_by_xpath = "//button[@type='submit']"
    logout_button_by_xpath = "//a[normalize-space()='Logout']"

    def __init__(self, driver):
        self.driver = driver

    def setUserEmail(self, userEmail):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.Email_textbox_by_xpath).clear()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.Email_textbox_by_xpath).send_keys(userEmail)

    def setUserPassword(self, password):
        self.driver.find_element(By.ID, self.Password_textbox_by_id).clear()
        self.driver.find_element(By.ID, self.Password_textbox_by_id).send_keys(password)

    def ClickSubmit(self):
        # Wait for the login button to be clickable
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.Login_button_by_xpath))
        ).click()

    def ClickLogout(self):
        # Wait for the logout button to be visible
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.logout_button_by_xpath))
        ).click()
