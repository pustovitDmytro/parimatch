from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from GetDates import GetDates
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By




BaseUrl = "https://www.parimatch.com/"

Select = "ФУТБОЛ. ЛИГА ЧЕМПИОНОВ УЕФА"
driver = webdriver.Firefox()
driver.get(BaseUrl)
driver.find_element_by_id("spArchive").click()
time.sleep(1)
days = GetDates("3.09.14","1.01.15",0)
for s in days:
    inputForm = driver.find_element_by_id("archItems")
    input  = inputForm.find_element_by_id("datePicker")
    link = inputForm.find_element_by_tag_name("a")
    input.send_keys(s)
    input.send_keys(Keys.ENTER)
    link.click()
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "f1")))
    finally:
        getTable(driver.page_source,Select)
driver.close()