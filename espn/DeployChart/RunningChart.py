from week_finder import *
from IntChart import *
from TotChart import *
from SackChart import *

def RushLeader_Score_Diff(team1, team2):
    start_week = 0
    end_week = get_college_football_week() - 1

    # Create an empty list to store DataFrames for each team
    selected_teams_Rushing_leader = []

    # Iterate through the specified weeks
    for week in range(start_week, end_week + 1):
        
        file_path = f'data/week{week}.csv'
        # Load data for the current week with the specified encoding
        current_week_data = pd.read_csv(file_path, encoding='ISO-8859-1')
        
        if current_week_data['Away Team'].isin([team1]).any():
            
            # Filter the games involving the selected teams and append to the list
            team1_games = current_week_data[((current_week_data['Away Team'] == team1)) &
                                            ~current_week_data['RushingLeader'].isna()].copy()
            team1_games['Team_IN'] = current_week_data['Away Team']
            team1_games['status'] = "Away Game"
            team1_games['vs'] = current_week_data['Home Team']

        elif current_week_data['Home Team'].isin([team1]).any():

            # Filter the games involving the selected teams and append to the list
            team1_games = current_week_data[((current_week_data['Home Team'] == team1)) &
                                            ~current_week_data['RushingLeader'].isna()].copy()
            team1_games['Team_IN'] = current_week_data['Home Team']
            team1_games['status'] = "Home Game"
            team1_games['vs'] = current_week_data['Away Team']

        if current_week_data['Away Team'].isin([team2]).any():

            # Filter the games involving the selected teams and append to the list
            team2_games = current_week_data[((current_week_data['Away Team'] == team2)) &
                                            ~current_week_data['RushingLeader'].isna()].copy()
            team2_games['Team_IN'] = current_week_data['Away Team']
            team2_games['status'] = "Away Game"
            team2_games['vs'] = current_week_data['Home Team']

        elif current_week_data['Home Team'].isin([team2]).any():

            # Filter the games involving the selected teams and append to the list
            team2_games = current_week_data[((current_week_data['Home Team'] == team2)) &
                                            ~current_week_data['RushingLeader'].isna()].copy()
            team2_games['Team_IN'] = current_week_data['Home Team']
            team2_games['status'] = "Home Game"
            team2_games['vs'] = current_week_data['Away Team']

        # Add the week information to the DataFrame
        team1_games['Week'] = team2_games['Week'] = week
        
        selected_teams_Rushing_leader.append(
            team1_games[['status', 'vs', 'RushingLeader', 'RushingLeaderScore', 'Week','Team_IN']])
        selected_teams_Rushing_leader.append(
            team2_games[['status', 'vs', 'RushingLeader', 'RushingLeaderScore', 'Week','Team_IN']])

    # Concatenate all DataFrames to create a single DataFrame for selected teams
    selected_teams_Rushing_leader_df = pd.concat(selected_teams_Rushing_leader)

    # Filter out Rushing leaders with less than 2 occurrences
    Rushing_leader_counts = selected_teams_Rushing_leader_df['RushingLeader'].value_counts()
    Rushing_leaders_to_include = Rushing_leader_counts[Rushing_leader_counts >= 2].index
    selected_teams_Rushing_leader_df = selected_teams_Rushing_leader_df[selected_teams_Rushing_leader_df['RushingLeader'].isin(Rushing_leaders_to_include)]
   
    # Plotting the line chart for RushingLeaderScore over the weeks for selected teams using plotly
    fig_selected_teams = px.line(selected_teams_Rushing_leader_df, x='Week', y='RushingLeaderScore',
                                color='Team_IN', line_group='RushingLeader', markers=True,
                                title=f'RushingLeaderScore Over Weeks for {team1} and {team2}',
                                labels={'RushingLeaderScore': 'RushingLeaderScore', 'Week': 'Week'},
                                hover_data=['status', 'vs', 'Team_IN'])

    fig_selected_teams.update_traces(
        hovertemplate='Week: %{x}<br>vs: %{customdata[1]}<br>Status: %{customdata[0]}<br>RushingLeaderScore: %{y}<br> Team: %{customdata[2]}'
    )

    # Show the plot for RushingLeaderScore over weeks for selected teams with 'vs' and 'Team' in the hover tooltip
    fig_selected_teams.show()
    
    # Display the interactive plot
    fig_selected_teams.write_html("/ESPN/RushingFig.html")

