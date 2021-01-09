from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


#Supremebot that searches the item through categories

PATH = '/Users/vaccari/PycharmProjects/pythonProject/drivers/chromedriver'

driver = webdriver.Chrome(PATH)
#Open the wanted category URL
driver.get('https://www.supremenewyork.com/shop/all/sweatshirts')

#Waits until the selected item and the colour chosen loads up and then clicks the item
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[contains(text(), "Rib Hooded")]/../following-sibling::p/a[contains(text(), "Chocolate")]')))
driver.find_element_by_xpath('//*[contains(text(), "Rib")]/../following-sibling::p/a[contains(text(), "Chocolate")]').click()

# Open the dropdown window for size
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'size')))
dropdownSize = driver.find_element_by_id('size')
item1 = Select(dropdownSize)

# Choose the size
item1.select_by_visible_text('Large')

# Add to cart
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-remove-buttons"]/input')))
driver.find_element_by_xpath('//*[@id="add-remove-buttons"]/input').click()

# checkout now
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cart"]/a[2]')))
driver.find_element_by_xpath('//*[@id="cart"]/a[2]').click()

# Now you have fill all your personal information
driver.find_element_by_id('order_billing_name').send_keys('name')
driver.find_element_by_id('order_email').send_keys('email')
driver.find_element_by_id('order_tel').send_keys('phone')
driver.find_element_by_id('bo').send_keys('street')
driver.find_element_by_id('order_billing_city').send_keys('City')
driver.find_element_by_id('order_billing_zip').send_keys('zip')

# Choosing the country
dropdownCountry = driver.find_element_by_id('order_billing_country')
country = Select(dropdownCountry)
country.select_by_visible_text('FINLAND')

# Credit Card info
driver.find_element_by_id('cnb').send_keys('111111111111')

# CcMonth
DropdownCcMonth = driver.find_element_by_id('credit_card_month')
month = Select(DropdownCcMonth)
month.select_by_index(10)

# CcYear
DropdownCcYear = driver.find_element_by_id('credit_card_year')
year = Select(DropdownCcYear)
year.select_by_index(0)

# CVV
driver.find_element_by_id('vval').send_keys('420')

# Accept the terms
driver.find_element_by_xpath('//*[@id="cart-cc"]/fieldset/p/label/div/ins').click()