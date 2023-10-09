from selenium import webdriver
from scrape_players_and_stats import *
import requests

def main(url, webdriver_path):
    # Initialize WebDriver
    driver = webdriver.Chrome()
    driver.get(url)

    try:
        scrape_players_and_stats(driver, url, webdriver_path)
    finally:
        # Close the WebDriver when done
        driver.quit()

if __name__ == "__main__":
    passing_url = 'https://www.espn.com/college-football/stats/player'
    
    rushing_url= 'https://www.espn.com/college-football/stats/player/_/view/offense/stat/rushing/table/rushing/sort/rushingYards/dir/desc'
    
    receiving_url='https://www.espn.com/college-football/stats/player/_/view/offense/stat/receiving/table/receiving/sort/receivingYards/dir/desc'
    
    defense_url='https://www.espn.com/college-football/stats/player/_/view/defense'
    
    special_return_url='https://www.espn.com/college-football/stats/player/_/view/special'
    
    kick_url='https://www.espn.com/college-football/stats/player/_/view/special/stat/kicking'
    
    punting_url='https://www.espn.com/college-football/stats/player/_/view/special/stat/punting'
    
    scoring_url='https://www.espn.com/college-football/stats/player/_/view/scoring'
    
    urls=[passing_url,
    rushing_url,receiving_url,defense_url,special_return_url,kick_url, punting_url,scoring_url]
    
    webdriver_path = 'E:/chromedriver_win32/chromedriver.exe'
    
    for url in urls:
        main(url, webdriver_path)
