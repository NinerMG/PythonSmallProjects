from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
#driver.get("https://www.amazon.com")
#driver.get("https://www.empik.com/droga-krolow-archiwum-burzowego-swiatla-tom-1-sanderson-brandon,p1578898967,ksiazka-p")
driver.get("https://python.org/")
# price_pln = driver.find_element(By.CLASS_NAME, value="css-1f0k13e-DesktopPriceStyles").text
# print(price_pln)

# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))

documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
print(documentation_link.text)

bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)


driver.close()      # closing tab
# driver.quit()       # closing browser