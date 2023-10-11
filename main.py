from selenium import webdriver
from scrape_players_and_stats import *
import requests
from get_url import *

def main( name,name2, name3):
    # Initialize WebDriver
    urls=get_url()
    webdriver_path = 'E:/chromedriver_win32/chromedriver.exe'
    driver = webdriver.Chrome()
    
    #for url in urls:
    #   driver.get(url)
    
    driver.get(urls[0])

    try:
        scrape_players_and_stats(driver, urls[0], webdriver_path,name,name2, name3)
    finally:
        # Close the WebDriver when done
        driver.quit()

