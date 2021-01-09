from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# SUPREME AUTOCHECKOUT BOT
# Optimized with selenium's explicit waits

# Bot still needs to be upgraded to find an item that has not been seen before
# Maybe change the bot to go straight to viewing all items without going to menu


PATH = '/Users/vaccari/PycharmProjects/pythonProject/drivers/chromedriver'

driver = webdriver.Chrome(PATH)

# Opens up the selected URL
driver.get('https://www.supremenewyork.com/shop/all')
driver.maximize_window()
# Searches waits and clicks the shop
#WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="wrap"]/nav/ul/li[4]/a')))
#driver.find_element_by_xpath('//*[@id="wrap"]/nav/ul/li[4]/a').click()
# searches and clicks the view all
#WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="nav-store"]/li[2]/a')))
#driver.find_element_by_xpath('//*[@id="nav-store"]/li[2]/a').click()
# Searches and clicks item
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="container"]/article[205]/div/a/img')))
driver.find_element_by_xpath('//*[@id="container"]/article[205]/div/a/img').click()
# Open the dropdown window for size
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'size')))
dropdownSize = driver.find_element_by_id('size')
item1 = Select(dropdownSize)
# Choose the size
item1.select_by_visible_text('Medium')
# Add to cart
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-remove-buttons"]/input')))
driver.find_element_by_xpath('//*[@id="add-remove-buttons"]/input').click()
# checkout now
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cart"]/a[2]')))
driver.find_element_by_xpath('//*[@id="cart"]/a[2]').click()
# Now you have fill all your personal information
driver.find_element_by_id('order_billing_name').send_keys('Ismo Taalasmaa')
driver.find_element_by_id('order_email').send_keys('ismo.taalasmaa@gmail.com')
driver.find_element_by_id('order_tel').send_keys('+1234567890')
driver.find_element_by_id('bo').send_keys('Pihlajakatu 420')
driver.find_element_by_id('order_billing_city').send_keys('Stadi')
driver.find_element_by_id('order_billing_zip').send_keys('42000')
# Choosing the country
dropdownCountry = driver.find_element_by_id('order_billing_country')
country = Select(dropdownCountry)
country.select_by_visible_text('FINLAND')
# Credit Card info
driver.find_element_by_id('cnb').send_keys('111111111111')
# CcMonth
DropdownCcMonth = driver.find_element_by_id('credit_card_month')
month = Select(DropdownCcMonth)
month.select_by_index(7)
# CcYear
DropdownCcYear = driver.find_element_by_id('credit_card_year')
year = Select(DropdownCcYear)
year.select_by_index(1)
# CVV
driver.find_element_by_id('vval').send_keys('420')
# Accept the terms
driver.find_element_by_xpath('//*[@id="cart-cc"]/fieldset/p/label/div/ins').click()
