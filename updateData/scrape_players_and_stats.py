from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from UpdateCSV import *
from scrape_header import *
from week_finder import *
from get_url import *
import time



def scrape_players_and_stats(driver, url, webdriver_path):
    # Rest of the code for scraping player names and stats
    # Click "Show More" repeatedly until it's not available
    while True:
        try:
            show_more_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'loadMore__link')))
            show_more_button.click()
            time.sleep(2)  # Introduce a delay to allow content to load
        except Exception as e:
            print("No more 'Show More' button found. Exiting.")
            break
    
    # Scrape player names and stats from the fully loaded page
    soup = BeautifulSoup(driver.page_source, 'lxml')
    players_chart = soup.find(class_='Table__TBODY')
    school_chart = soup.find( class_='Table__TBODY')
    
    # Scrape player names
    player_tags = players_chart.find_all('a')
    players = [tag.get_text() for tag in player_tags]
    
    # Scrape school names
    school_tags = school_chart.find_all('span')
    schools = [tag_s.get_text() for tag_s in school_tags]
    # Scrape player stats
    tbody_elements = soup.find_all(class_='Table__TBODY')
    header=scrape_header(driver)

    if len(tbody_elements) >= 2:
        second_players_chart = tbody_elements[1]
        td_elements = second_players_chart.find_all('td', class_='Table__TD')
        
        # Initialize a list to group statistics in sets of 11
        num_headers = len(header)
        grouped_stats_dict = {header[i]: [] for i in range(0,num_headers)}
        header_index=-1
        
        
        for index, td_element in enumerate(td_elements):
            player_stat = td_element.get_text()
            header_index=header_index+1
            # Add the player_stat to the current group
            if header_index >= len(header):
                header_index=0
                grouped_stats_dict[header[header_index]].append([player_stat])         
            else:
                grouped_stats_dict[header[header_index]].append([player_stat])
    
    #saving player data to csv
    urls=get_url() 
    
    if url == urls[0]:
            name="data/passing.csv"
            UpdateCSV(players,schools,grouped_stats_dict,name)
            
    elif url == urls[1]:
            name="data/rushing.csv"
            UpdateCSV(players,schools,grouped_stats_dict,name)
            
        
    elif url == urls[2]:
            name="data/receiving.csv"
            UpdateCSV(players,schools,grouped_stats_dict,name)
            
        
    elif url == urls[3]:
            name="data/defense.csv" 
            UpdateCSV(players,schools,grouped_stats_dict,name)
    