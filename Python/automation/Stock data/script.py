import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd
import os
import sys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from datetime import datetime
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

path = './chromedriver.exe'
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
application_path = os.path.dirname(sys.executable)
website = "https://finance.yahoo.com/"

StockList = [
    "Mahindra & Mahindra Limited",
    "BHEL.NS",
    "Exide Industries Limited",
    "Godrej Industries Limited",
    "Hindustan Aeronautics Limited",
    "ITC Limited",
    "Larsen & Toubro Limited",
    "Steel Authority of India Limited",
    "The Tata Power Company Limited"
]

stockCurrentPrice = []
stockChangeAmt = []
stockLossPercent = []
StockNameList = []
delay = 15
waitTime = WebDriverWait(driver,10)


now = datetime.now()
month_date_year = now.strftime("%m%d%y")#mmddyyyy


def btnClick():
    try:
        searchBtn = driver.find_element(By.XPATH,
                                        value = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/button[2]")
        searchBtn.send_keys(Keys.ENTER)

    except Exception as e:

        print("got exeception error on btn click: "+e)


def searchStock(stockname):
    try:
        searchField = driver.find_element(By.XPATH,
                                         value = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/input[1]")
        searchField.send_keys(stockname)
        btnClick()
        try:



            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@id ="quote-header-info"]')))
           # stockCurrentPriceValue = driver.find_element(by="xpath", value = "//div[@class='D(ib) Mend(20px)']/fin-streamer[@data-field='reregularMarketPrice']").text
            #stockCurrentPriceValue = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH,'/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[6]/div[1]/div[3]/div[1]/div[1]/fin-streamer[1]')))
            #stockCurrentPriceValue = waitTime.until(lambda driver: driver.find_element(by='xpath',value='/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[6]/div[1]/div[3]/div[1]/div[1]/fin-streamer[1]')).text
            #newStockPriceVar = stockCurrentPriceValue.text()
            #driver.implicitly_wait(15)

            stockCurrentPriceValue = driver.find_element(By.XPATH,
                                                         value='//div[@id ="quote-header-info"]/div/div/div/fin-streamer[1]').text

            stockChangeAmtValue = driver.find_element(By.XPATH,
                                                      value='//div[@id ="quote-header-info"]/div/div/div/fin-streamer[2]').text

            stockLossPercentvalue = driver.find_element(By.XPATH,
                                                        value='//div[@id ="quote-header-info"]/div/div/div/fin-streamer[3]').text

            driver.implicitly_wait(10)

            stockCurrentPrice.append(stockCurrentPriceValue)
            stockChangeAmt.append(stockChangeAmtValue)
            stockLossPercent.append(stockLossPercentvalue)

        except Exception as e:
            print("exceptionm at find stock data"+str(e))


    except Exception as e:
        print("got exeception error: on searchStock "+str(e))




for stockName in StockList:
    try:
        driver.get(website)
        time.sleep(5)
        searchStock(stockName)
        print(stockName+": done")
        StockNameList.append(stockName)
        time.sleep(7)
    except Exception as e:
        print("got execetion at looping for stock values"+e)


stock_dict = {"stockname": stockName, "StockPrice": stockCurrentPrice,"stockChange": stockChangeAmt,"StockChangePerc": stockLossPercent}

df_headline = pd.DataFrame(stock_dict)
fileName = f'StockReport-{month_date_year}.csv'
finalPath = os.path.join(application_path,fileName)
df_headline.to_csv(finalPath)
driver.quit()

#/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]

# share price = /html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[6]/div[1]/div[3]/div[1]/div[1]/fin-streamer[1]
#share change = /html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[6]/div[1]/div[3]/div[1]/div[1]/fin-streamer[2]
# share percent change = /html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[6]/div[1]/div[3]/div[1]/div[1]/fin-streamer[3]