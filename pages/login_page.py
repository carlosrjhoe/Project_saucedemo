from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    URL = 'https://www.saucedemo.com/'

    def __init__(self, driver):
        self.driver = driver
        self.title = (By.CLASS_NAME, 'login_logo')

    def open_login_page(self):
        self.driver.get(self.URL)

    def title_login_page(self):
        wait = WebDriverWait(self.driver, 2)
        value = wait.until(EC.visibility_of_element_located((self.title)))
        return value.text