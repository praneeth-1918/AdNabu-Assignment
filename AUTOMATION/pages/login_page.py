from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):

# Locators
password_input = (By.ID, "Password")
enter_button = (By.XPATH, "//button[@type='submit']")

def enter_password(self, password):
self.send_keys(self.password_input, password)

def submit_password(self):
self.click(self.enter_button)

def login(self, password):
self.enter_password(password)
self.submit_password()
