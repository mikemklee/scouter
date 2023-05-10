import time

import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession

from scouters import AirForceOneScouter


RETRY_IN_SECONDS = 10


airforce_scouter = AirForceOneScouter()


# start search
while True:
    print("Checking @ Footlocker...")
    size_found = airforce_scouter.check_footlocker()
    airforce_scouter.report_search_result(size_found)

    print("Checking @ Nike...")
    size_found = airforce_scouter.check_nike()
    airforce_scouter.report_search_result(size_found)

    print(f"Checking again in {RETRY_IN_SECONDS} seconds...")
    time.sleep(RETRY_IN_SECONDS)
