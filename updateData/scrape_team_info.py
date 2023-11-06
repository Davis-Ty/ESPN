import re
from bs4 import BeautifulSoup
from week_finder import *


def scrape_team_info(driver):
    
        def process_player_data(player_data):
            split_player_data = re.findall(r"([A-Za-z\s]+)(\d+)", player_data)
            player_info_dict = {}

            # Define labels for different player roles
            player_roles = ['PassingLeader', 'RushingLeader', 'ReceivingLeader']

            for i, (player_name, player_stats) in enumerate(split_player_data, start=1):
                # Determine the player role based on the index
                player_role = player_roles[i - 1]
                
                # Create keys like 'PassingLeader1', 'RushingLeader2', and so on
                player_info_dict[f'{player_role}'] = player_name.strip()
                player_info_dict[f'{player_role}Score'] = player_stats

            return player_info_dict

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

        # Iterate through info_list in chunks of 6
        for i in range(0, len(info_list), 6):
            Score = info_list[i + 2]
            away_team, home_team = Score.split(',')

            # Split away team and home team into team and score
            away_team_letters = re.search(r'[A-Za-z\s]+', away_team)
            away_team_score = re.search(r'\d+', away_team)

            home_team_letters = re.search(r'[A-Za-z\s]+', home_team)
            home_team_score = re.search(r'\d+', home_team)

            # Adjust the index to get the next two elements for player data
            players_info_dict = process_player_data(info_list[i + 3] + info_list[i + 4] + info_list[i + 5])

            info = {
                'Team': info_list[i],
                'Opo Team': info_list[i + 1],
                'Away Team': away_team_letters.group().strip() if away_team_letters else '',
                'Away Team Score': away_team_score.group() if away_team_score else '',
                'Home Team': home_team_letters.group().strip() if home_team_letters else '',
                'Home Team Score': home_team_score.group() if home_team_score else '',
            }

            # Update the info dictionary with player data
            info.update(players_info_dict)

            info_list_dict.append(info)

        # Return the result as a list of dictionaries
        return info_list_dict
