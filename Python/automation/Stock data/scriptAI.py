import time
import os
import sys
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

# Path to Chrome WebDriver executable
webdriver_path = './chromedriver.exe'

# Initialize the WebDriver
service = Service(executable_path=webdriver_path)
driver = webdriver.Chrome(service=service)

# Website URL
website = "https://finance.yahoo.com/"

# List of stock names or symbols
stock_list = [
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

# Lists to store stock data
stock_data = []

# Create a timestamp for the CSV file name
timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

# Function to click the search button
def click_search_button():
    try:
        search_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Search')]")
        search_button.click()
    except Exception as e:
        print("Error clicking search button:", str(e))

# Function to search for a stock
def search_stock(stock_name):
    try:
        search_field = driver.find_element(By.XPATH, "//input[@name='yfin-usr-qry']")
        search_field.clear()
        search_field.send_keys(stock_name)
        click_search_button()

        # Wait for the stock data to load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[text()='Add to watchlist']")))

        # Extract stock data
        stock_current_price = driver.find_element(By.XPATH, "//td[text()='Open']/following-sibling::td").text
        stock_change_amt = driver.find_element(By.XPATH, "//td[text()='Change']/following-sibling::td").text
        stock_loss_percent = driver.find_element(By.XPATH, "//td[text()='% Change']/following-sibling::td").text

        stock_data.append({
            "Stock Name": stock_name,
            "Stock Price": stock_current_price,
            "Change Amount": stock_change_amt,
            "Loss Percent": stock_loss_percent
        })

    except Exception as e:
        print("Error searching for stock:", str(e))

# Iterate through the stock list and fetch data
for stock_name in stock_list:
    driver.get(website)
    time.sleep(3)  # Add a short delay to allow the page to load
    search_stock(stock_name)
    print(f"Fetched data for: {stock_name}")
    time.sleep(5)  # Add a delay between stock searches

# Save the data to a CSV file
output_file = f'StockReport-{timestamp}.csv'
output_path = os.path.join(os.getcwd(), output_file)
df = pd.DataFrame(stock_data)
df.to_csv(output_path, index=False)
print(f"Data saved to {output_path}")

# Quit the WebDriver
driver.quit()
