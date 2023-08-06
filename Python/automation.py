from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

driver.get('https://youtube.com')

searchbox = driver.find_element(By.XPATH,('//*[@id="search"]'))

print(searchbox)


searchbox.send_keys('Kunal Choudhary')

searchbtn = driver.find_element(By.XPATH,('//*[@id="search-icon-legacy"]'))
searchbtn.click()