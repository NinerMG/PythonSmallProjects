from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


URL = "https://en.wikipedia.org/wiki/Main_Page"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url=URL)

# using XPATH
#editor_number = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/ul/li[2]/a[1]')
#print(editor_number.text)

# using CSS Selectors
article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount > ul > li:nth-child(2) > a:nth-child(1)")
# article_count.click()

# find element by Link Text
all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

# find the "Search" <input> by Name
search = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "search")))
search.send_keys("Python", Keys.ENTER)
