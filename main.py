import smtplib

import requests
import lxml
from bs4 import BeautifulSoup
URL ="https://www.amazon.com/-/es/Reproductor-multimedia-transmisi%C3%B3n-inal%C3%A1mbrica-controles/dp/B0916TKFF2/ref=lp_16225007011_1_2"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0",
    "Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3"
}
response = requests.get(URL, headers=header)
#respose binario
soup= BeautifulSoup(response.content, "lxml")

price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
title = soup.find(id="productTitle").get_text()
BUY_PRICE = 30

if price_as_float<BUY_PRICE:
    message = f"{title} is now {price}"
    # with smtplib.SMTP("smtp.mail.yahoo.com", port=465) as connection:
    #     connection.starttls()
    #     result = connection.login("email@yahoo.com", "password")
    #     connection.sendmail(
    #         from_addr="email",
    #         to_addrs="email",
    #         msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}"
    # )
print("send")