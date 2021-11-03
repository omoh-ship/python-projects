import requests
import lxml
import smtplib
from bs4 import BeautifulSoup

AMAZON_URL = "https://www.amazon.com/HP-Touchscreen-i5-1135G7-Streaming-14-dw1024nr/" \
             "dp/B091D6F3JP/ref=sr_1_4?dchild=1&keywords=hp+ssd+laptop+with+pen&qid=1632748735&sr=8-4"

MY_EMAIL = "lomimine8@gmail.com"
MY_PASSWORD = "lomimine^^309"

headers = {
    "User-Agent": "Defined",
}

response = requests.get(url=AMAZON_URL, headers=headers)
web_xml = response.text

soup = BeautifulSoup(web_xml, "lxml")
# price = soup.find(name="span", class_="a-size-medium a-color-price priceBlockBuyingPriceString")
price_tag = soup.find(id="priceblock_ourprice").getText().split("$")
price = float(price_tag[1])
item_name = soup.find(id="productTitle").getText()
if price < 500:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="gloriaisedu@gmail.com",
            msg=f"Subject: Amazon Price Alert\n\n{item_name} is now {price}.",
        )
# print(price)

