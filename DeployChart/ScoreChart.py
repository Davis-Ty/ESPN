#load data
import pandas as pd
import plotly.express as px
from week_finder import *

def Score_Diff(away_team1,away_team2 ):
    # Define the range of weeks you want to consider
    start_week = 0
    end_week = get_college_football_week() - 1

    # Create an empty list to store DataFrames for each week
    all_team_games = []

    # Assuming school_td_totals['School'] is a list of teams
    for team in [away_team1, away_team2]:
        # Iterate through the specified weeks
        for week in range(start_week, end_week + 1):
            file_path = f'data/week{week}.csv'
            # Load data for the current week with the specified encoding
            current_week_data = pd.read_csv(file_path, encoding='ISO-8859-1')

            # Filter the games involving the current team and append to the list
            team_games = current_week_data[current_week_data['Away Team'] == team].copy()
            team_games['Score Difference'] = team_games['Away Team Score'] - team_games['Home Team Score']
            
            # Add the week information to the DataFrame
            team_games['Week'] = week

            all_team_games.append(team_games[['Team', 'Away Team', 'Away Team Score', 'Home Team', 'Home Team Score', 'Score Difference', 'Week']])

    # Concatenate all DataFrames to create a single DataFrame for all teams
    all_teams_result_df = pd.concat(all_team_games)

    # Plotting the line chart for all teams using plotly
    fig = px.line(all_teams_result_df, x='Week', y='Score Difference', color='Home Team', markers=True,
                title='Week-by-Week Score Difference for Selected Teams',
                labels={'Score Difference': 'Score Difference', 'Week': 'Week'})
                


    # Add annotations for the 'Away Team' names
    for index, row in all_teams_result_df.iterrows():
        vs_team = row['Away Team']
        fig.add_annotation(x=row['Week'], y=row['Score Difference'], text=vs_team,
                        showarrow=True, arrowhead=4, ax=0, ay=-40)

    # Update the legend item for "Home Team" to "vs"
    fig.update_layout(legend_title_text='vs')

    # Show the plot
    fig.show()