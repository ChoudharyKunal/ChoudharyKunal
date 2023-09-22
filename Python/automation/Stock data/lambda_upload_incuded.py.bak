import json
import boto3
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime
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

start = time.time()

print(23*2.3)

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


# Initialize S3 and SMTP clients
s3_client = boto3.client('s3')
smtp_port = 587
smtp_server = "smtp.gmail.com"
my_mail = "choudharykunal474@gmail.com"
passcode = "jnhdldttiwnelmfv"
email_list = ["baisoyakunal69@gmail.com", "choudharykunal474@gmail.com"]

def lambda_handler(event, context):
    try:
        # Set up S3 resource
        s3 = boto3.resource('s3')
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

            cwd = '/tmp'
            df_headline = pd.DataFrame(stock_dict)
            finalPath = os.path.join(cwd,filename_create())
            df_headline.to_csv(finalPath)
            driver.quit()
            
            upload_to_s3(latest_filename)
            print("File uploaded to S3")


        # Create the filename
        latest_filename = filename_create()
        
        # Download the file from S3
        s3.meta.client.download_file('dailystockreportdata', 'StockReport-092023.csv', f'/tmp/{latest_filename}')
        print(f"File downloaded successfully: {latest_filename}")

        # Send emails to recipients
        send_emails(email_list, latest_filename)
        print("Data sent")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

def upload_to_s3(filename):
    try:
        s3_client = boto3.client('s3')
        bucket_name = 'dailystockreportdata'  # Replace with your S3 bucket name
        object_key = f'stock-reports/{filename}'  # Modify the object key as needed

        s3_client.upload_file(f'/tmp/{filename}', bucket_name, object_key)

    except Exception as e:
        print(f"An error occurred while uploading to S3: {str(e)}")
        
def filename_create():
    now = datetime.now()
    month_date_year = now.strftime("%m%d%y")
    filename = f'StockReport-{month_date_year}.csv'
    return filename
    

    
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




        except Exception as e:
            print("exceptionm at find stock data"+str(e))

            StockNameList.append(stockName)

            stockCurrentPrice.append("Null")
            stockChangeAmt.append("Null")
            stockLossPercent.append("Null")


    except Exception as e:
        print("got exeception error: on searchStock "+str(e))




def send_emails(email_list, latest_filename):
    try:
        for person in email_list:
            subject = f"Daily Stock Data Report for {latest_filename}"
            
            # Email body
            body = f"""
            Hi Subscriber,
            
            Please find today's stock data report attached below as {latest_filename}. 
            
            Thanks and Regards,
            The Stock Reporter
            """

            # Create a MIME object to define parts of the email
            msg = MIMEMultipart()
            msg["From"] = my_mail
            msg["To"] = person
            msg["Subject"] = subject

            # Attach the body of the message
            msg.attach(MIMEText(body, 'plain'))

            # Open and encode the file as base64
            with open(f'/tmp/{latest_filename}', 'rb') as attachment:
                attachment_package = MIMEBase('application', 'octet-stream')
                attachment_package.set_payload(attachment.read())
                encoders.encode_base64(attachment_package)
                attachment_package.add_header('Content-Disposition', f'attachment; filename={latest_filename}')
                msg.attach(attachment_package)

            # Convert message to string
            text = msg.as_string()

            # Connect to the SMTP server
            print("Connecting to server...")
            TIE_server = smtplib.SMTP(smtp_server, smtp_port)
            TIE_server.starttls()
            TIE_server.login(my_mail, passcode)
            print("Connected to server")

            # Sending email to person
            print(f"Sending email to: {person}")
            TIE_server.sendmail(my_mail, person, text)
            print(f"Successfully sent email to: {person}")

        TIE_server.quit()
    except Exception as e:
        print(f"An error occurred while sending emails: {str(e)}")

