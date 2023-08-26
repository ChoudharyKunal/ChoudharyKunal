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
website = "https://finance.yahoo.com/"

StockList = ["TCS.NS","M&M.NS"]
def btnClick():
    try:
        searchBtn = driver.find_element(by="xpath",
                                        value="/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/button[2]")
        searchBtn.click()
    except Exception as e:
        print("got exeception error on btn click: "+e)


def searchStock(stockname):
    try:
        searchField = driver.find_element(by="xpath",
                                         value="/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/input[1]")

   #     searchField1 = driver.find_element(by="xpath", value='//form[1]/input[1]')
        searchField.send_keys(stockname)

        btnClick()

    except Exception as e:
        print("got exeception error: on searchStock "+e)


driver.get(website)

for stockName in StockList:
    try:
        searchStock(stockName)
        time.sleep(5)
        print(stockName+": done")
        time.sleep(10)
    except Exception as e :
        print("got execetion at looping for stock values"+e)

#search_btn.click()

#seach_field = driver.find_element(by="xpath", value = '//input[@class = "input-KLRTYDjH"')

#seach_field.send_keys("TCS")\

driver.close()

