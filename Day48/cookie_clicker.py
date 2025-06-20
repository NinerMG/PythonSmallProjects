from selenium import webdriver
from selenium.webdriver.common.by import By
import time

URL = "https://orteil.dashnet.org/experiments/cookie/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url=URL)

# Get cookie
cookie = driver.find_element(By.ID, value="cookie")

# get upgrade items id
items = driver.find_elements(By.CSS_SELECTOR, value="#store div")
items_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 5
five_min = time.time() + 60*5 #5 minutes

while True:
    cookie.click()

    #Every 5 seconds
    if time.time() > timeout:

        #get all upgrade <b> tags
        all_prices = driver.find_elements(By.CSS_SELECTOR, value="#store b")
        item_prices = []

        #Convert <b> text into an integer price
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        # create dictionary of store items and prices
        cookie_upgrades = {}
        for item in items:
            item_id = item.get_attribute("id")
            price_tag = item.find_element(By.TAG_NAME, "b")
            if price_tag.text != "":
                try:
                    price = int(price_tag.text.split("-")[1].strip().replace(",", ""))
                    cookie_upgrades[price] = item_id
                except (IndexError, ValueError):
                    continue

        # Get current cookie count
        money_element = driver.find_element(by=By.ID, value="money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        # Find upgrades that we can currently afford
        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id

        # Purchase the most expensive affordable upgrade
        if affordable_upgrades:
            highest_price_affordable_upgrade = max(affordable_upgrades)
            to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]
            driver.find_element(by=By.ID, value=to_purchase_id).click()



        # Add another 5 seconds until the next check
        timeout = time.time() + 5

        # After 5 minutes stop the bot and check the cookies per second count.
    if time.time() > five_min:
        cookie_per_s = driver.find_element(by=By.ID, value="cps").text
        print(cookie_per_s)
        break