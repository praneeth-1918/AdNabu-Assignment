from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from .base_page import BasePage

class SearchPage(BasePage):

# Locators
search_icon = (By.XPATH, "//a[contains(@href,'search')]")
search_box = (By.NAME, "q")
first_product = (By.CSS_SELECTOR, ".grid__item a")

def search_product(self, product_name):
self.click(self.search_icon)
self.send_keys(self.search_box, product_name)
self.get_element(self.search_box).send_keys(Keys.RETURN)

def select_first_product(self):
self.click(self.first_product)
