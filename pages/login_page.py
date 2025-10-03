from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class LoginPage:
    URL = 'https://www.saucedemo.com/'

    def __init__(self, driver):
        self.driver = driver
        self.title = (By.CLASS_NAME, 'login_logo')
        self.product_title = (By.CLASS_NAME, 'title')
        self.buton = (By.ID, 'login-button')
        self.id_username = (By.ID, 'user-name')
        self.id_password = (By.ID, 'password')
        self.username = 'standard_user'
        self.password = 'secret_sauce'

    def open_swag_page(self):
        self.driver.get(self.URL)

    def title_access_page(self):
        wait = WebDriverWait(self.driver, 2)
        value = wait.until(EC.visibility_of_element_located((self.title)))
        return value.text

    def title_product_page(self):
        wait = WebDriverWait(self.driver, 2)
        value = wait.until(EC.visibility_of_element_located((self.product_title)))
        return value.text

    def set_username(self,):
        element = WebDriverWait(self.driver, 2).until(
            EC.visibility_of_element_located((self.id_username)))
        element.send_keys(self.username)

    def set_password(self):
        element = WebDriverWait(self.driver, 2).until(
            EC.visibility_of_element_located((self.id_password)))
        element.send_keys(self.password)

    def click_buton_login(self):
        element = self.driver.find_element(*self.buton)
        element.click()
