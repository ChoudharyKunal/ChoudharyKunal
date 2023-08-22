import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd
import os
import sys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


path = './chromedriver.exe'
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)

application_path = os.path.dirname(sys.executable)
website = "https://in.tradingview.com/chart/XkvxZBGi/"

driver.get(website)

#search_btn = driver.find_element(by="xpath", value = '//div/button[@class = "tv-header-search-container tv-header-search-container__button tv-header-search-container__button--full js-header-search-button"]')

#search_btn.click()

#seach_field = driver.find_element(by="xpath", value = '//input[@class = "input-KLRTYDjH"')

#seach_field.send_keys("TCS")

driver.implicitly_wait(1000)