import time

import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession

PRODUCT_PAGE_NIKE = "https://www.nike.com/ca/t/air-force-1-07-shoes-rWtqPn/CW2288-111"
PRODUCT_PAGE_FOOTLOCKER = "https://www.footlocker.ca/en/product/~/4100960.html"

MY_SIZE = "9.0"

RETRY_IN_SECONDS = 10


session = HTMLSession()


def check_footlocker():
    response = requests.get(PRODUCT_PAGE_FOOTLOCKER)
    soup = BeautifulSoup(response.text, "html.parser")

    def custom_validator(string: str):
        return string and string.endswith(MY_SIZE)

    return soup.find_all(
        "button",
        attrs={"class": "Button SizeSelector-button"},
        string=custom_validator,
    )


def check_nike():
    response = session.get(PRODUCT_PAGE_NIKE)

    # render JS stuff
    response.html.render()

    raw_html = response.html.html
    soup = BeautifulSoup(raw_html, "html.parser")

    def custom_validator(tag):
        not_disabled = not tag.has_attr("disabled")
        id_match = tag.has_attr("id") and tag["id"].startswith("skuAndSize")
        value_match = tag.has_attr("value") and tag["value"].endswith(MY_SIZE)

        return not_disabled and id_match and value_match

    return soup.find_all(custom_validator)


def report_search_result(found: bool):
    message = f"My size {MY_SIZE} found!!!" if found else "My size not found :("
    print(f"\t{message}")


# start search
while True:
    print("Checking @ Footlocker...")
    size_found = check_footlocker()
    report_search_result(size_found)

    print("Checking @ Nike...")
    size_found = check_nike()
    report_search_result(size_found)

    print(f"Checking again in {RETRY_IN_SECONDS} seconds...")
    time.sleep(RETRY_IN_SECONDS)
