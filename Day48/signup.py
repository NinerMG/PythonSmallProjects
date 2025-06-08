from selenium import webdriver
from selenium.webdriver.common.by import By


URL = "https://secure-retreat-92358.herokuapp.com"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url=URL)

first_name = driver.find_element(By.NAME, value="fName")
last_name = driver.find_element(By.NAME, value="lName")
email_address = driver.find_element(By.NAME, value="email")
submit = driver.find_element(By.CSS_SELECTOR, value="form button")

first_name.send_keys("Maciek")
last_name.send_keys("Tester")
email_address.send_keys("maciek@tester.com")
submit.click()

