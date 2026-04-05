from selenium.webdriver.common.by import By
from .base_page import BasePage

class ProductPage(BasePage):

add_to_cart_btn = (By.NAME, "add")
cart_icon = (By.XPATH, "//a[contains(@href,'cart')]")

def add_to_cart(self):
self.click(self.add_to_cart_btn)

def is_cart_visible(self):
return self.get_element(self.cart_icon).is_displayed()
