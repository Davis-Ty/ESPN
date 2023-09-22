import requests
from bs4 import BeautifulSoup
import time


# URL of the page to scrape
url = "https://www.espn.com/college-football/stats/player"

# Send a GET request with a user agent header
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'
}
response = requests.get(url, headers=headers)



# Check if the request was successful
if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all <a> elements with class "AnchorLink"
        anchor_tags = soup.find_all('a', class_='AnchorLink')

        # Extract player names from the <a> elements
        player_names = [tag.text for tag in anchor_tags if 'data-player-uid' in tag.attrs]

        # Print the player names
        for index, name in enumerate(player_names, start=1):
            print(f"{index}. {name}")
else:
        print('Failed to retrieve the webpage.')

        # Add a delay before quitting
        time.sleep(1)