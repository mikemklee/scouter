import time


from scouters import AirForceOneScouter


from plyer import notification

RETRY_IN_SECONDS = 10


airforce_scouter = AirForceOneScouter()


# start search
while True:
    print("Checking @ Footlocker...")
    size_found = airforce_scouter.check_footlocker()
    airforce_scouter.report_search_result(size_found)

    notification.notify(
        title="Found size",
        message="Found a size at Footlocker!",
        app_name="Scouter",
    )

    print("Checking @ Nike...")
    size_found = airforce_scouter.check_nike()
    airforce_scouter.report_search_result(size_found)

    notification.notify(
        title="Found size",
        message="Found a size at Nike!",
        app_name="Scouter",
    )

    print(f"Checking again in {RETRY_IN_SECONDS} seconds...")
    time.sleep(RETRY_IN_SECONDS)
