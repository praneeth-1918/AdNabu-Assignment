from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 10)

driver.get("https://adnabuteststore.com")

# Search product
search = wait.until(EC.presence_of_element_located((By.NAME, "search")))
search.send_keys("shirt")
search.send_keys(Keys.RETURN)

# Select product
product = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".product-item")))
product.click()

# Add to cart
add_btn = wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart")))
add_btn.click()

# Validate cart
cart = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "cart-count")))
assert int(cart.text) > 0

driver.quit()
