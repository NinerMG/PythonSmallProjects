import requests
from bs4 import BeautifulSoup
import smtplib

PRODUCT_URL = "https://www.amazon.com/GIGABYTE-GeForce-WINDFORCE-Graphics-GV-N5060WF2OC-8GD/dp/B0F8LDHQ7Y/ref=sr_1_3?_encoding=UTF8&dib=eyJ2IjoiMSJ9.FfV2RMcDFDB3cidk_723NRIXfGjf66-TOCibO856KzpN74IaIZZ2aYPdvxlKwLnESHCDliR856IfBPzj_jvLPeo4dQr24kAyqyJgcIBFez1cFgf6twPsNLJXD6-eOFV_NI6uA2JKaIzyWZY8PcH7ZpEDCbW78cS-MXM-xNRb4Qer1BpVzIF4wWE1zbK-Qp4Q2eDokxiy4V6amqbKcB_1i-zCDruiojoSRv6eNpsufqY.l-6uzzXGKsgRKsfYphTpF5mVTb5RTMWvIgT_9I76HTs&dib_tag=se&keywords=graphics+cards&qid=1749291645&sr=8-3"
HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "pl,en-US;q=0.9,en;q=0.8,de;q=0.7",
    "Priority": "u=0, i",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 OPR/119.0.0.0",
    "X-Amzn-Trace-Id": "Root=1-68440f3b-4d61ae91622051861cf7731a"
}

SMTP_EMAIL = ""
SMTP_PASSWORD = ""


response = requests.get(url=PRODUCT_URL, headers=HEADERS)
response.raise_for_status()
response_text = response.text

soup = BeautifulSoup(response_text, 'html.parser')


price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("$")[1]

price_as_float = float(price_without_currency)
# print(price_as_float)

# ====================== Send an Email ===========================
# Get the product title
title = soup.find(id="productTitle").get_text().strip()


# Set the price below which you would like to get a notification
MINIMUM_PRICE = 2000

if price_as_float < MINIMUM_PRICE:
    message = f"{title}\n is on SALE for {price}!"

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        result = connection.login(SMTP_EMAIL, SMTP_PASSWORD)
        connection.sendmail(
            from_addr=SMTP_EMAIL,
            to_addrs=SMTP_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{PRODUCT_URL}".encode("utf-8")
        )
    print("mail was send")