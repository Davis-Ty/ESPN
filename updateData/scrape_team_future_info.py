import re
from bs4 import BeautifulSoup
from week_finder import *

def scrape_team_future_info(driver):
    # Parse the page source with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'lxml')

    # Find all divs with class 'ScheduleTables'
    schedule_tables_list = soup.find_all(class_='ScheduleTables')

    # Initialize a list to store the extracted information
    info_list = []

    # Iterate through each ScheduleTables element and extract information
    for schedule_tables in schedule_tables_list:
        # Find all <tr> elements within the current ScheduleTables
        tr_elements = schedule_tables.find_all('tr', class_='Table__TR')

        for tr in tr_elements:
            # Find all <td> elements within the <tr> element
            td_elements = tr.find_all('td')
            for td in td_elements:
                info_list.append(td.get_text(strip=True))

    # Initialize a list to store the dictionaries
    info_list_dict = []

    # Iterate through info_list in chunks of 5
    for i in range(0, len(info_list), 6):
        team = info_list[i]
        
        # Split the team into away and home teams
        teams = team.split('@')

        # Check if there are exactly two parts after splitting
        if len(teams) == 2:
            away_team, home_team = teams
        else:
            # Handle the case where the team name doesn't contain '@'
            away_team, home_team = teams[0], ''  # For example, set away_team to the full team name and home_team to an empty string or another appropriate value
        
        info = {
            'Away Team': away_team.strip(),
            'Home Team': info_list[i + 1],
            'Time': info_list[i + 2],
            'TV':info_list[i + 3],
            'Tickets': info_list[i + 4]
        }

        info_list_dict.append(info)

    # Return the result as a list of dictionaries
    return info_list_dict
