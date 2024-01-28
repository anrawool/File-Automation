import __meta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import datetime
import pandas as pd

# /usr/lib/chromium-browser/chromedriver


def fetch_timetable(make_file=False):
    s = Service("./geckodriver")

    driver = webdriver.Firefox(service=s)
    driver.get("https://fiitjee-eschool.com/timetable.html")

    dropdownbox = driver.find_elements(by=By.TAG_NAME, value="Option")
    i = 0
    while i < len(dropdownbox):
        if dropdownbox[i].text == "FeSCF327A1R":
            dropdownbox[i].click()
        i += 1

    data = []

    tbody = driver.find_element(
        By.XPATH, "/html/body/div/div[6]/div/div/div/div[2]/div/div[16]/div/table/tbody"
    )
    for tr in tbody.find_elements(By.XPATH, "//tr"):
        row = [
            item.text for item in tr.find_elements(By.XPATH, ".//td") if item.text != ""
        ]
        data.append(row)

    data = [item for item in data if len(item) != 0]
    data = pd.DataFrame(data, index=None, columns=["Date", "Day", "Class 1", "Class 2"])

    if make_file:
        data.to_csv(f"timetable_{datetime.datetime.now()}.csv")

    return data
