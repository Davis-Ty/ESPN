#load data
import pandas as pd
import plotly.express as px
from week_finder import *

def RushLeader_Score_Diff(team1,team2):
    # Define the range of weeks you want to consider
    start_week = 0
    end_week = get_college_football_week() - 2

    # Create an empty list to store DataFrames for each team
    selected_teams_rushing_leader = []

    # Iterate through the specified weeks
    for week in range(start_week, end_week + 1):
        file_path = f'data/week{week}.csv'
        # Load data for the current week with the specified encoding
        current_week_data = pd.read_csv(file_path, encoding='ISO-8859-1')

        # Filter the games involving the selected teams and append to the list
        team1_games = current_week_data[(current_week_data['Away Team'] == team1) &
                                        ~current_week_data['RushingLeader'].isna()].copy()
        
        team2_games = current_week_data[(current_week_data['Away Team'] == team2)  &
                                        ~current_week_data['RushingLeader'].isna()].copy()

        # Add the week information to the DataFrame
        team1_games['Week'] = team2_games['Week'] = week

        selected_teams_rushing_leader.append(team1_games[['Away Team', 'Home Team', 'RushingLeader', 'RushingLeaderScore', 'Week']])
        selected_teams_rushing_leader.append(team2_games[['Away Team', 'Home Team', 'RushingLeader', 'RushingLeaderScore', 'Week']])

    # Concatenate all DataFrames to create a single DataFrame for selected teams
    selected_teams_rushing_leader_df = pd.concat(selected_teams_rushing_leader)

    # Plotting the line chart for PassingLeaderScore over the weeks for selected teams using plotly
    fig_selected_teams = px.line(selected_teams_rushing_leader_df, x='Week', y='RushingLeaderScore', color='RushingLeader', markers=True,
                                title=f'RushingLeaderScore Over Weeks for {team1} and {team2}',
                                labels={'RushingLeaderScore': 'RushingLeaderScore', 'Week': 'Week'},
                                hover_data={'Away Team', 'Home Team', 'Week'})

    # Rename the 'Home Team' and 'Away Team' columns to 'vs' and 'Team' respectively
    fig_selected_teams.update_traces(hovertemplate='Week: %{x}<br>Team: %{customdata[1]}<br>vs: %{customdata[0]}<br>RushingLeaderScore: %{y}')

    # Show the plot for PassingLeaderScore over weeks for selected teams with 'vs' and 'Team' in the hover tooltip
    fig_selected_teams.show()