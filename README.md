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
- Run espn/updateData/main.py To update data to current information.
- Run espn/DeployChart/RadarChart.py To deploy D3 Chart.
  
# TESTBED
 - [View the ESPN.football.ipynb file ](https://github.com/Kaireega/ESPN-WebScraping/blob/codespace-shiny-potato-grxp46qwg4v3j7g/ESPN.football.ipynb)
 - or
   - Run espn/DeployChart/RadarChart.py To deploy D3 Chart
 # Questions that can be answered from the testbed
 - Overall Defensive Performance:

Which teams have the strongest overall defensive performance based on aggregated statistics?
- Category-specific Insights:

What teams excel in specific defensive categories, such as Solo Tackles, Sacks, Interceptions, or Forced Fumbles?
-Comparative Analysis:

How do two selected teams compare in terms of overall defensive performance and specific defensive categories?
- Opponent Vulnerabilities:

What defensive weaknesses do upcoming opponents exhibit, and how can these be exploited strategically?
- Threshold Analysis:

Which teams meet or exceed a user-defined threshold for a specific defensive category, and how does this impact their overall performance?
- Game-specific Insights:

How does a team's defensive performance vary from game to game, and are there patterns related to specific opponents?

- Fan Engagement:

What defensive statistics are most engaging for fans, and how can the program enhance fan understanding and interaction with the team's performance?

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



# Components:

- Writeup: fewer than 2800 words, 12pt font, typed. Describe in depth the novelties of your approach and your     discoveries/insights/experiments, etc.  


# Grading scheme & Submission instructions

- Writeup
[2%] Introduction - Motivation

[3%] Problem definition

[5%] Survey

  


- Experiments/ Evaluation
  
[5%] Description of your testbed; list of questions your experiments are designed to answer

[25%] Details of the experiments; observations (as many as you can!)

[5%] Conclusions and discussion


[-5% if not included] Distribution of team member effort. Can be as simple as "all team member contributes a similar amount of effort". If effort distribution is too uneven, I may assign higher scores to members who contributed more.

[10%] Team’s contact person submits one zip file, called teamXXfinal.zip, via D2L, where XX is the team number (e.g., team01final.zip for team 1). 


DOC - a folder called DOC (short for “documentation”) containing:

teamXXreport.pdf - Your report writeup in PDF format (can be created using any software, e.g., latex, Word)

teamXXposter.pdf - Your final poster. (if any)


