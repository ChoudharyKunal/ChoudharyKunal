import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd
import os
import sys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import robot
import selenium.webdriver.support.expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

path = './chromedriver.exe'
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)

application_path = os.path.dirname(sys.executable)
website = "https://in.tradingview.com/"

driver.get(website)

driver.find_element(by="xpath", value='/html[1]/body[1]/div[3]/div[3]/div[2]/div[3]/button[1]').click()
time.sleep(5)


#signin = driver.find_element(by="xpath", value='//div[@class="menuBox-Kq3ruQo8"]/div/button[1]')

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='menuBox-Kq3ruQo8']/div/button[1"))).click()


time.sleep(5)


#search_btn.click()

#seach_field = driver.find_element(by="xpath", value = '//input[@class = "input-KLRTYDjH"')

#seach_field.send_keys("TCS")\

driver.close()

