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
website = "https://www.youtube.com/"

driver.get(website)

application_text = driver.find_element(by="xpath", value='//input[@id="search"]')
valueToSearch = input("Enter Value for YouTube Search: ")
application_text.send_keys(valueToSearch)

search_btn = driver.find_element(by="xpath", value='//button[@id="search-icon-legacy"]')

search_btn.click()
driver.implicitly_wait(10)
driver.execute_script("window.scrollTo(0,4000)")

ytVideoContainer = driver.find_elements(by="xpath", value='//body/ytd-app[1]/div[1]/ytd-page-manager[1]/ytd-search[1]/div[1]/ytd-two-column-search-results-renderer[1]/div[1]/ytd-section-list-renderer[1]/div[2]/ytd-item-section-renderer[1]/div[3]/ytd-video-renderer')

videoTitle = []
videoViews = []
videoLink = []

for videos in ytVideoContainer:
        titlaValue = videos.find_element(by="xpath", value=".//div[1]/div[1]/div[1]/div[1]/h3[1]").text
        vLink = videos.find_element(by="xpath",value='.//div[1]/div[1]/div[1]/div[1]/h3[1]/a[1]').get_attribute("href")
        vViews = videos.find_element(by="xpath", value='.//div[1]/ytd-video-meta-block[1]/div[1]/div[2]/span[1]').text
        videoTitle.append(titlaValue)
        videoLink.append(vLink)
        videoViews.append(vViews)

        ActionChains.key_down(Keys.LEFT_CONTROL).click(vLink).key_up(Keys.LEFT_CONTROL).build().perform()
        time.sleep(3)

ytDict = {'title':videoTitle, 'Views': videoViews, "Video Link": videoLink}

df_headlines = pd.DataFrame(ytDict)

filename =f'{valueToSearch}.csv'
##final_path = os.path.join(application_path,filename)
df_headlines.to_csv(filename)

#driver.save_screenshot("seearch_result.png")
#driver.quit()

#//div[@class = "style-scope ytd-video-renderer"]
#//div[@class = "style-scope ytd-video-meta-block"]/span
#//yt-formatted-string[@class = "style-scope ytd-video-renderer"].text()

#------------------------------------------------------

#new title xpath
#//*[@id="contents"]/ytd-video-renderer
#//body/ytd-app[1]/div[1]/ytd-page-manager[1]/ytd-search[1]/div[1]/ytd-two-column-search-results-renderer[1]/div[1]/ytd-section-list-renderer[1]/div[2]/ytd-item-section-renderer[1]/div[3]/ytd-video-renderer[1]/div[1]/div[1]
#//body/ytd-app[1]/div[1]/ytd-page-manager[1]/ytd-search[1]/div[1]/ytd-two-column-search-results-renderer[1]/div[1]/ytd-section-list-renderer[1]/div[2]/ytd-item-section-renderer[1]/div[3]/ytd-video-renderer[1]/div[1]/div[1]---main text body
#//body/ytd-app[1]/div[1]/ytd-page-manager[1]/ytd-search[1]/div[1]/ytd-two-column-search-results-renderer[1]/div[1]/ytd-section-list-renderer[1]/div[2]/ytd-item-section-renderer[1]/div[3]/ytd-video-renderer[1]/div[1]/div[1]/div[1]/div[1]/h3[1]--title pane
#//body/ytd-app[1]/div[1]/ytd-page-manager[1]/ytd-search[1]/div[1]/ytd-two-column-search-results-renderer[1]/div[1]/ytd-section-list-renderer[1]/div[2]/ytd-item-section-renderer[1]/div[3]/ytd-video-renderer[1]/div[1]/div[1]/div[1]/div[1]/h3[1]/a[1]--get url
#//body/ytd-app[1]/div[1]/ytd-page-manager[1]/ytd-search[1]/div[1]/ytd-two-column-search-results-renderer[1]/div[1]/ytd-section-list-renderer[1]/div[2]/ytd-item-section-renderer[1]/div[3]/ytd-video-renderer[1]/div[1]/div[1]/div[1]/ytd-video-meta-block[1]/div[1]/div[2]/span[1]
#//div[@id="metadata-line"]/span[109]--view coint