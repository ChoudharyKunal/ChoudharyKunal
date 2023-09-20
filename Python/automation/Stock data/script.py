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
from selenium.webdriver.common.action_chains import ActionChains
import sendingEmailwithAttachment

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
action = ActionChains(driver)
email_list = ["baisoyakunal69@gmail.com","choudharykunal474@gmail.com"]


now = datetime.now()
month_date_year = now.strftime("%m%d%y")#mmddyyyy

def filename_create():
    now = datetime.now()
    month_date_year = now.strftime("%m%d%y")  # mmddyyyy
    fileName = f'StockReport-{month_date_year}.csv'
    return fileName

def btnClick():
    try:
        searchBtn = driver.find_element(By.XPATH,
                                        value='//form[@class="Pos(r)"]/button[@type="submit"]')

        searchBtn.send_keys(Keys.ENTER)
        #driver.send_keys(Keys.ENTER)
        driver.implicitly_wait(15)
    except Exception as e:

        print("got exeception error on btn click: "+e)


def searchStock(stockname):
    try:
        searchField = driver.find_element(By.XPATH,'//form[@class="Pos(r)"]/input[1]')
        searchField.send_keys(stockname)
        print(stockname+" has been filled in value")
        driver.find_element(By.XPATH,
                            value='//form[@class="Pos(r)"]/button[@type="submit"]').click()
        #btnClick()
        print("button is clicked")
        driver.implicitly_wait(15)

        try:



            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//div[@id ="quote-header-info"]')))


            stockCurrentPriceValue = driver.find_element(By.XPATH,
                                                         value='//div[@id ="quote-header-info"]/div/div/div/fin-streamer[1]').text

            stockChangeAmtValue = driver.find_element(By.XPATH,
                                                      value='//div[@id ="quote-header-info"]/div/div/div/fin-streamer[2]').text

            stockLossPercentvalue = driver.find_element(By.XPATH,
                                                        value='//div[@id ="quote-header-info"]/div/div/div/fin-streamer[3]').text

            driver.implicitly_wait(10)
            StockNameList.append(stockName)

            stockCurrentPrice.append(stockCurrentPriceValue)
            stockChangeAmt.append(stockChangeAmtValue)
            stockLossPercent.append(stockLossPercentvalue)

           # print(len(StockNameList)+':'+len(stockCurrentPriceValue)+':'+len(stockChangeAmtValue)+':'+len(stockLossPercent))


        except Exception as e:
            print("exceptionm at find stock data"+str(e))

            StockNameList.append(stockName)

            stockCurrentPrice.append("Null")
            stockChangeAmt.append("Null")
            stockLossPercent.append("Null")


    except Exception as e:
        print("got exeception error: on searchStock "+str(e))




for stockName in StockList:
    try:
        driver.get(website)
        driver.implicitly_wait(15)
        searchStock(stockName)
        print(stockName+": done")
        time.sleep(7)
    except Exception as e:
        print("got execetion at looping for stock values"+str(e))



stock_dict = {"stockname": StockList, "StockPrice": stockCurrentPrice,"stockChange": stockChangeAmt,"StockChangePerc": stockLossPercent}

cwd = os.getcwd()
df_headline = pd.DataFrame(stock_dict)
#fileName = f'StockReport-{month_date_year}.csv'
finalPath = os.path.join(cwd,filename_create())
df_headline.to_csv(finalPath)
driver.quit()

print("starting to send mails")
sendingEmailwithAttachment.send_emails(email_list,filename_create())

print("done with sending mails")