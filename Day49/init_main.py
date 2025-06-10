from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

ACCOUNT_EMAIL = ""
ACCOUNT_PASSWORD = ""

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

URL = ("https://www.linkedin.com/jobs/search/?currentJobId=4230849127&distance=25&f"
       "_AL=true&geoId=103348205&keywords="
       "Python%20Developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&sortBy=R")

# get to page with job offers
driver = webdriver.Chrome(options=chrome_options)
driver.get(url=URL)
wait = WebDriverWait(driver, 10)
time.sleep(2)

# click on sign in
sign_in = driver.find_element(By.CSS_SELECTOR, value="#base-contextual-sign-in-modal > div > section > div > div > div > div.sign-in-modal > button")
sign_in.click()

time.sleep(2)

# add data
email_field = driver.find_element(By.ID, value="base-sign-in-modal_session_key")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element(By.ID, value="base-sign-in-modal_session_password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)

# save job offer for later
time.sleep(3)



all_listenings = driver.find_elements(By.CSS_SELECTOR, "li.scaffold-layout__list-item")

for job_offer in all_listenings:
    try:
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", job_offer)
        time.sleep(0.5)
        job_offer.click()
        time.sleep(1)
    except Exception as e:
        print(f"Nie udało się kliknąć w ofertę pracy: {e}")
        continue
    try:
        save_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
        "#main > div > div.scaffold-layout__list-detail-inner.scaffold-layout__list-detail-inner--grow > div.scaffold-layout__detail.overflow-x-hidden.jobs-search__job-details > div > div.jobs-search__job-details--container > div > div.job-view-layout.jobs-details > div:nth-child(1) > div > div:nth-child(1) > div > div.relative.job-details-jobs-unified-top-card__container--two-pane > div > div.mt4 > div > button")))
        save_button.click()
        time.sleep(1)
    except NoSuchElementException:
        pass