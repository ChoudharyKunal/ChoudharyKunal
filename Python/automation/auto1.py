from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd
from datetime import datetime
import os
import sys

application_path = os.path.dirname(sys.executable) #getting path od executable file for the script

now = datetime.now()

month_date_year = now.strftime("%m%d%y")#mmddyyyy


options = Options()
options.headless = True
path = './chromedriver.exe'
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options = options)

website = "https://www.thesun.co.uk/sport/football/"



driver.get(website)

containers = driver.find_elements(by="xpath", value='//div[@class="teaser__copy-container"]')
titles = []
subtitles = []
links = []

for container in containers:
    titleValue = container.find_element(by="xpath", value='.//a/span').text
    subtitleValue = container.find_element(by="xpath", value='.//a/h3').text
    Link = container.find_element(by="xpath", value='.//a').get_attribute("href")#getting the href attribute fro the /a tag
    titles.append(titleValue)
    subtitles.append(subtitleValue)
    links.append(Link)

my_dict = {'titles':titles, 'subtitles':subtitles, 'links': links}
df_headline = pd.DataFrame(my_dict)

filename = f'headlines-{month_date_year}.csv'
final_path = os.path.join(application_path,filename)
df_headline.to_csv(final_path)

driver.quit()

#//div[@class="teaser__copy-container"]/a/span
#//div[@class="teaser__copy-container"]/a/h3
#//div[@class="teaser__copy-container"]/a

#/html/body/div[3]/main/div/div[2]/div/div[3]/div/div[2]/a/h3