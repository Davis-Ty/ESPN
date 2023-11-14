from UpdateWeekCSV import *
from scrape_team_info import *
from week_finder import *
from vs_who_url import *
from scrape_team_future_info import *

def team_vs_team(driver, url, webdriver_path):
    #saving player data to csv
    urls=vs_who_url() 

    for i in range (0,len(urls)):
        if url==urls[i] :  
            if i<get_college_football_week():       
                # Scrape info 
                data=scrape_team_info(driver)
                
                name=f"/espn/data/week{i}.csv"
                UpdateWeekCSV(data,name)
            else: 
                # Scrape info 
                data1=scrape_team_future_info(driver)
    
                name=f"/espn/data/week{i}.csv"
                UpdateWeekCSV(data1,name)
   