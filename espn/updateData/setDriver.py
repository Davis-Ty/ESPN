from selenium import webdriver
from scrape_players_and_stats import *
import requests
from get_url import *
from vs_who_url import *
from team_vs_team import *

from selenium.webdriver.chrome.options import *

def setDriver():
    
    
        urls=get_url()
        vs_url=vs_who_url()
        # Initialize WebDriver
        
        #put your chrome driver path
        webdriver_path = 'E:/chromedriver_win32/chromedriver.exe'
       
        driver = webdriver.Chrome()
        try:
                for url in urls:
                        driver.get(url)
                        scrape_players_and_stats(driver, url, webdriver_path)
                
                for url in vs_url:
                        driver.get(url)
                        team_vs_team(driver, url, webdriver_path)          
     
        finally:
                        # Close the WebDriver when done
                        driver.quit()

