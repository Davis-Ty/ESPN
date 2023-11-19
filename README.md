# ESPN Data and Visual Analytics
# DESCRIPTION 

The football analytics dashboard sources its data from a CSV file named "defense.csv," encompassing diverse defensive metrics across various college football teams. With a visually engaging dark-themed layout, the dashboard features a navigation bar housing links to "About" and "Contact" sections. The main dashboard section, titled "2023 Football Defensive Stats," showcases a variety of charts for visualizing defensive statistics.

Among the primary charts, the stacked bar chart (id='allD-chart') presents aggregated defensive statistics for different college football teams, with interactive capabilities for potential data filtering based on the x-axis range. The scatter chart (id='football-chart') employs football symbols ('🏈') to represent each team, symbol size dynamically reflecting corresponding defensive statistic values. The radar chart (id='radar-chart') facilitates the comparison of selected defensive metrics for two chosen teams through polygons, illustrating performance across various defensive categories.

The dashboard offers interactive controls, including dropdowns and sliders for users to select defensive statistic categories and compare teams. A slider enables users to adjust a threshold value, filtering teams based on the chosen defensive statistic. Team selection dropdowns empower users to choose two teams for direct defensive performance comparison.

Additionally, the application incorporates hidden charts (Passing, Running, Sack, Score, Total, Total Histogram) that become visible upon users selecting two teams, providing detailed insights into specific facets of the game.

Thematically, the application employs football-inspired colors, utilizing green for the background, yellow for text, and random colors for charts. The navigation bar includes external links to web pages offering additional information under "About" and "Contact."

- Team Strengths and Weaknesses:

Identify specific defensive areas where teams excel or struggle, offering crucial insights into their strengths and weaknesses.
- Player Performance:

Evaluate individual player contributions to leading Offensive statistics, enabling teams and coaches to recognize standout performers and areas for improvement.
- Tactical Adjustments:

Coaches can use the detailed defensive metrics to make informed tactical adjustments, optimizing strategies based on the strengths and weaknesses revealed in the data.
- Opponent Analysis:

Gain a competitive edge by studying the defensive performance of upcoming opponents. Teams can tailor their offensive strategies to exploit identified weaknesses in the opposition's defense.
- Game Predictions:

Leverage historical defensive data to make predictions about future games. Analyzing trends and patterns can contribute to more accurate forecasts of team performance.

- Fan Engagement:

Enhance fan engagement by providing visual and easily understandable defensive statistics. Fans can gain deeper insights into their favorite team's performance and engage in data-driven discussions.
- Overall Team Performance:

Evaluate the overall defensive performance of a team across multiple categories. This information is valuable for assessing a team's competitiveness and potential success in the league.
- Scouting Opponents:

Scout opposing teams to understand their defensive strategies and key players. This knowledge can be crucial in developing effective offensive game plans.
# INSTALLATION 
- Chrome:

Download ChromeDriver from the official site: ChromeDriver Downloads.
Make sure to download the version that matches your Chrome browser version.
After downloading, you may need to add the ChromeDriver executable to your system's PATH or provide the path to it in your Selenium script.
- pip install Flask
- pip install beautifulsoup4
- pip install selenium
- pip install pandas
- pip install plotly
- pip install dash
- pip install dash-bootstrap-components
- pip install requests

# EXECUTION 
- After installing all needed elements
- go to E:\espn\updateData\setDriver.py file
- change the webdriver_path veriable to your chrome driver path that is on your computer.
- Run espn/updateData/main.py (To update data to current information).
- Run espn/DeployChart/RadarChart.py (To deploy D3 Chart/webpage).
  
# DATA SOURCE
https://www.espn.com/college-football/stats

# Team Members
- Tyon Davis
- Kairee Gay
- Kiana Forbes
- Victoria Ramirez-Garcia
- Cameron Davis
# Class INFO
Data and Visual Analytics Section 01 Fall Semester 2023 CO

This is a detailed description of what we did, what results we obtained, and what we have learned and/or can conclude from our work.
