from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup
driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 15)

try:
# Open site
driver.get("https://adnabu-store-assignment1.myshopify.com/")

# 🔐 Step 1: Enter password (Shopify password page)
password_input = wait.until(EC.presence_of_element_located((By.ID, "Password")))
password_input.send_keys("AdnabuQA")

enter_button = driver.find_element(By.XPATH, "//button[@type='submit']")
enter_button.click()

# 🛍️ Step 2: Search for a product
search_icon = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href,'search')]")))
search_icon.click()

search_box = wait.until(EC.presence_of_element_located((By.NAME, "q")))
search_box.send_keys("shirt")
search_box.send_keys(Keys.RETURN)

# 🧾 Step 3: Select first product
product = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".grid__item a")))
product.click()

# 🛒 Step 4: Add to cart
add_to_cart = wait.until(EC.element_to_be_clickable((By.NAME, "add")))
add_to_cart.click()

# ✅ Step 5: Validate cart (drawer or page)
cart = wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(@href,'cart')]")))

print("✅ Test Passed: Product added to cart successfully")

except Exception as e:
print("❌ Test Failed:", str(e))

finally:
driver.quit(
