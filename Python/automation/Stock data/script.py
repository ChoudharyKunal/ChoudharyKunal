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
from selenium.webdriver.common.keys import Keys

path = './chromedriver.exe'
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)

application_path = os.path.dirname(sys.executable)
website = "https://finance.yahoo.com/"

StockList = ["TCS.NS","M&M.NS"]
stockCurrentPrice = []
stockLossAmt = []
stockLossPercent = []


def btnClick():
    try:
        searchBtn = driver.find_element(by="xpath",
                                        value="/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/button[2]")
        searchBtn.send_keys(Keys.ENTER)
    except Exception as e:
        print("got exeception error on btn click: "+e)


def searchStock(stockname):
    try:
        searchField = driver.find_element(by="xpath",
                                         value="/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/input[1]")
        searchField.send_keys(stockname)
        btnClick()
        time.sleep(10)
        stockCurrentPriceValue = driver.find_element(by="xpath", value = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[6]/div[1]/div[3]/div[1]/div[1]/fin-streamer[1]').text
        stockLossAmtValue = driver.find_element(by="xpath", value = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[6]/div[1]/div[3]/div[1]/div[1]/fin-streamer[2]').text
        stockLossPercentvalue = driver.find_element(by="xpath", value = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[6]/div[1]/div[3]/div[1]/div[1]/fin-streamer[3]').text

        stockCurrentPrice.append(stockCurrentPriceValue)
        stockLossAmt.append(stockLossAmtValue)
        stockLossPercent.append(stockLossPercentvalue)




    except Exception as e:
        print("got exeception error: on searchStock "+e)




for stockName in StockList:
    try:
        driver.get(website)
        time.sleep(5)
        searchStock(stockName)
        print(stockName+": done")
        time.sleep(10)
    except Exception as e :
        print("got execetion at looping for stock values"+e)



driver.close()

#/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]

# share price = /html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[6]/div[1]/div[3]/div[1]/div[1]/fin-streamer[1]
#share change = /html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[6]/div[1]/div[3]/div[1]/div[1]/fin-streamer[2]
# share percent change = /html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[6]/div[1]/div[3]/div[1]/div[1]/fin-streamer[3]