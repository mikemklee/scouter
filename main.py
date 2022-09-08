import time

import requests
from bs4 import BeautifulSoup

PRODUCT_PAGE_FOOTLOCKER = "https://www.footlocker.ca/en/product/~/4100960.html"
MY_SIZE_FOOTLOCKER = "09.5"
RETRY_IN_SECONDS = 10

while True:
    response = requests.get(PRODUCT_PAGE_FOOTLOCKER)
    soup = BeautifulSoup(response.text, "html.parser")

    my_size_option = soup.find_all(
        "button",
        attrs={"class": "Button SizeSelector-button"},
        string=MY_SIZE_FOOTLOCKER,
    )

    if my_size_option:
        print(f"My size {MY_SIZE_FOOTLOCKER} found!")
        break
    else:
        print(f"My size not found... checking again in {RETRY_IN_SECONDS} seconds")
        time.sleep(RETRY_IN_SECONDS)
