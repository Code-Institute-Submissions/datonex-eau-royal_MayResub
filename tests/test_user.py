# Generated by Selenium IDE
import pytest
import time
import json
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

if os.path.isfile("test_env.py"):
    import test_env


class TestUserFunctionality():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_registration(self):
        username = os.environ.get("USERNAME")
        email = os.environ.get("EMAIL")
        password = os.environ.get("PASSWORD")
        self.driver.get("https://eau-royal.herokuapp.com/")
        self.driver.set_window_size(1920, 1080)
        self.driver.find_element(By.ID, "user-account-button").click()
        self.driver.find_element(By.LINK_TEXT, "Register").click()
        self.driver.find_element(By.ID, "id_username").send_keys(username)
        self.driver.find_element(By.ID, "id_email").click()
        self.driver.find_element(By.ID, "id_email").send_keys(email)
        self.driver.find_element(By.ID, "id_password1").click()
        self.driver.find_element(By.ID, "id_password1").send_keys(password)
        self.driver.find_element(By.ID, "id_password2").click()
        self.driver.find_element(By.ID, "id_password2").send_keys(password)
        self.driver.find_element(
            By.XPATH, "//button[contains(.,\'Sign Up\')]").click()
        time.sleep(3)

    def test_user_login(self):
        email = os.environ.get("EMAIL")
        password = os.environ.get("PASSWORD")
        self.driver.get("https://eau-royal.herokuapp.com/")
        self.driver.set_window_size(1920, 1080)
        self.driver.find_element(By.ID, "user-account-button").click()
        self.driver.find_element(By.LINK_TEXT, "Login").click()
        self.driver.find_element(By.ID, "id_login").send_keys(email)
        self.driver.find_element(
            By.ID, "id_password").send_keys(password)
        self.driver.find_element(
            By.XPATH, "(//button[@type=\'submit\'])[3]").click()
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, ".btn-danger").click()
        time.sleep(3)

    def test_user_logout(self):
        self.test_user_login()
        self.driver.find_element(By.ID, "user-account-button").click()
        self.driver.find_element(By.LINK_TEXT, "Logout").click()
        self.driver.find_element(
            By.XPATH, "//button[contains(.,\'Sign Out\')]").click()
        time.sleep(5)

    def test_user_shopping_instance(self):
        self.test_user_login()
        full_name = os.environ.get('FULL_NAME')
        phone_number = os.environ.get('PHONE_NUMBER')
        address_line_1 = os.environ.get('ADDRESS_LINE_1')
        town = os.environ.get('TOWN')
        country = os.environ.get('COUNTRY')
        card_number = os.environ.get('CARD_NUMBER')
        expiry_date = os.environ.get('EXPIRY_DATE')
        cvc = os.environ.get('CVC')
        self.driver.find_element(
            By.XPATH, "//h2[contains(.,\'Shop Now\')]").click()
        self.driver.find_element(By.CSS_SELECTOR, ".text-lg-right").click()
        time.sleep(2)
        self.driver.find_element(
            By.XPATH, "//img[@alt=\'adidas victory league\']").click()
        self.driver.find_element(
            By.XPATH, "//label[contains(.,\'30 ML\')]").click()
        self.driver.find_element(
            By.XPATH, "//input[@value=\'Add to Bag\']").click()
        self.driver.find_element(
            By.XPATH, "//span[contains(.,\'Continue Shopping\')]").click()
        self.driver.find_element(
            By.XPATH, "//img[@alt=\'burberry mr. burberry\']").click()
        self.driver.find_element(
            By.XPATH, "//label[contains(.,\'100 ML\')]").click()
        self.driver.find_element(
            By.XPATH, "//input[@value=\'Add to Bag\']").click()
        self.driver.find_element(
            By.CSS_SELECTOR, "#shopping-bag-button path").click()
        self.driver.find_element(
            By.CSS_SELECTOR, "#bag-md .col-12 .text-capitalize").click()
        self.driver.find_element(
            By.XPATH,  "//span[contains(.,\'Begin Checkout\')]").click()
        self.driver.find_element(By.ID, "id_full_name").send_keys(full_name)
        self.driver.find_element(By.ID, "id_phone_number").click()
        self.driver.find_element(
            By.ID, "id_phone_number").send_keys(phone_number)
        self.driver.find_element(By.ID, "save-details").click()
        self.driver.find_element(By.ID, "id_street_address1").click()
        self.driver.find_element(
            By.ID, "id_street_address1").send_keys(address_line_1)
        self.driver.find_element(By.ID, "id_town_or_city").click()
        self.driver.find_element(
            By.ID, "id_town_or_city").send_keys(town)
        target = self.driver.find_element_by_id('id_country')
        target.location_once_scrolled_into_view
        time.sleep(0.5)
        self.driver.find_element(By.ID, "id_country").click()
        dropdown = self.driver.find_element(By.ID, "id_country")
        dropdown.find_element(
            By.XPATH, f"//option[. = '{country}']").click()
        self.driver.find_element(By.ID, "save-delivery").click()
        time.sleep(2)
        target = self.driver.find_element_by_id('submit-button')
        target.location_once_scrolled_into_view
        time.sleep(2)
        frame = self.driver.find_element(
            By.XPATH, "//iframe[@title=\'Secure card payment input frame\']")
        time.sleep(1)
        self.driver.switch_to.frame(frame)
        time.sleep(1)
        self.driver.find_element(
            By.NAME, "cardnumber").click()
        self.driver.find_element(
            By.XPATH, "//input[@name=\'cardnumber\']").send_keys(card_number)
        self.driver.find_element(
            By.XPATH, "//input[@name=\'exp-date\']").send_keys(expiry_date)
        self.driver.find_element(
            By.XPATH, "//input[@name=\'cvc\']").send_keys(cvc)
        time.sleep(2)
        self.driver.switch_to.default_content()
        self.driver.find_element(
            By.XPATH, "//button[contains(.,\'Place Order\')]").click()
        time.sleep(5)

    def test_view_order_history(self):
        self.test_user_login()
        self.driver.find_element(By.ID, "user-account-button").click()
        self.driver.find_element(By.LINK_TEXT, "My Profile").click()
        time.sleep(3)
        self.driver.find_element(By.LINK_TEXT, "View order").click()
        time.sleep(3)
        self.driver.find_element(
            By.XPATH, "(//a[contains(@href, \'/profile/\')])[4]").click()
        time.sleep(2)
