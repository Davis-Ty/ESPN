from week_finder import *
from IntChart import *
from TotChart import *
from SackChart import *

def PassLeader_Score_Diff(team1, team2):
    start_week = 0
    end_week = get_college_football_week() - 1

    # Create an empty list to store DataFrames for each team
    selected_teams_passing_leader = []

    # Iterate through the specified weeks
    for week in range(start_week, end_week + 1):
        
        file_path = f'data/week{week}.csv'
        # Load data for the current week with the specified encoding
        current_week_data = pd.read_csv(file_path, encoding='ISO-8859-1')

        if current_week_data['Away Team'].isin([team1]).any():

            # Filter the games involving the selected teams and append to the list
            team1_games = current_week_data[((current_week_data['Away Team'] == team1)) &
                                            ~current_week_data['PassingLeader'].isna()].copy()
            team1_games['Team_IN'] = current_week_data['Away Team']
            team1_games['status'] = "Away Game"
            team1_games['vs'] = current_week_data['Home Team']

        elif current_week_data['Home Team'].isin([team1]).any():

            # Filter the games involving the selected teams and append to the list
            team1_games = current_week_data[((current_week_data['Home Team'] == team1)) &
                                            ~current_week_data['PassingLeader'].isna()].copy()
            team1_games['Team_IN'] = current_week_data['Home Team']
            team1_games['status'] = "Home Game"
            team1_games['vs'] = current_week_data['Away Team']

        if current_week_data['Away Team'].isin([team2]).any():

            # Filter the games involving the selected teams and append to the list
            team2_games = current_week_data[((current_week_data['Away Team'] == team2)) &
                                            ~current_week_data['PassingLeader'].isna()].copy()
            team2_games['Team_IN'] = current_week_data['Away Team']
            team2_games['status'] = "Away Game"
            team2_games['vs'] = current_week_data['Home Team']

        elif current_week_data['Home Team'].isin([team2]).any():

            # Filter the games involving the selected teams and append to the list
            team2_games = current_week_data[((current_week_data['Home Team'] == team2)) &
                                            ~current_week_data['PassingLeader'].isna()].copy()
            team2_games['Team_IN'] = current_week_data['Home Team']
            team2_games['status'] = "Home Game"
            team2_games['vs'] = current_week_data['Away Team']

        # Add the week information to the DataFrame
        team1_games['Week'] = team2_games['Week'] = week
        
        selected_teams_passing_leader.append(
            team1_games[['status', 'vs', 'PassingLeader', 'PassingLeaderScore', 'Week','Team_IN']])
        selected_teams_passing_leader.append(
            team2_games[['status', 'vs', 'PassingLeader', 'PassingLeaderScore', 'Week','Team_IN']])

    # Concatenate all DataFrames to create a single DataFrame for selected teams
    selected_teams_passing_leader_df = pd.concat(selected_teams_passing_leader)

    # Filter out passing leaders with less than 2 occurrences
    passing_leader_counts = selected_teams_passing_leader_df['PassingLeader'].value_counts()
    passing_leaders_to_include = passing_leader_counts[passing_leader_counts >= 2].index
    selected_teams_passing_leader_df = selected_teams_passing_leader_df[selected_teams_passing_leader_df['PassingLeader'].isin(passing_leaders_to_include)]
   
    # Plotting the line chart for PassingLeaderScore over the weeks for selected teams using plotly
    fig_selected_teams = px.line(selected_teams_passing_leader_df, x='Week', y='PassingLeaderScore',
                                color='PassingLeader', markers=True,
                                title=f'PassingLeaderScore Over Weeks for {team1} and {team2}',
                                labels={'PassingLeaderScore': 'PassingLeaderScore', 'Week': 'Week'},
                                hover_data=['status', 'vs','Team_IN'])

    fig_selected_teams.update_traces(
        hovertemplate='Week: %{x}<br>vs: %{customdata[1]}<br>Status: %{customdata[0]}<br>PassingLeaderScore: %{y}<br> Team: %{customdata[2]}'
    )

    # Show the plot for PassingLeaderScore over weeks for selected teams with 'vs' and 'Team' in the hover tooltip
    fig_selected_teams.show()
    # Display the interactive plot
    fig_selected_teams.write_html("/ESPN/PassingFig.html")

    # Concatenate all DataFrames to create a single DataFrame for selected teams
    selected_teams_passing_leader_df = pd.concat(selected_teams_passing_leader)

    # Sort the DataFrame by 'PassingLeaderScore' column in ascending order
    selected_teams_passing_leader_df.sort_values(by='PassingLeaderScore', ascending=True, inplace=True)

    # Assuming selected_teams_passing_leader_df is your DataFrame
    leader_counts = selected_teams_passing_leader_df.groupby(['Team_IN', 'PassingLeader']).size().reset_index(name='Count')

    
    # Filter the counts for Team1 and Team2
    team1_counts = leader_counts[leader_counts['Team_IN'] == team1]
    team2_counts = leader_counts[leader_counts['Team_IN'] == team2]

    # Get the PassingLeader with the highest count for Team1 and Team2
    team1_highest_count_leader = team1_counts.loc[team1_counts['Count'].idxmax(), 'PassingLeader']
    team2_highest_count_leader = team2_counts.loc[team2_counts['Count'].idxmax(), 'PassingLeader']

    # Get the row with the highest PassingLeaderScore for the most frequent PassingLeader from Team1 and Team2
    team1_highest_score_row = selected_teams_passing_leader_df[
        (selected_teams_passing_leader_df['Team_IN'] == team1) &
        (selected_teams_passing_leader_df['PassingLeader'] == team1_highest_count_leader)].nlargest(1,
                                                                                                       'PassingLeaderScore')
    team2_highest_score_row = selected_teams_passing_leader_df[
        (selected_teams_passing_leader_df['Team_IN'] == team2) &
        (selected_teams_passing_leader_df['PassingLeader'] == team2_highest_count_leader)].nlargest(1,
                                                                                                       'PassingLeaderScore')

    # Extract Home Team names
    team1_highest_home_team = team1_highest_score_row['vs'].values[0]
    team2_highest_home_team = team2_highest_score_row['vs'].values[0]

    # Get the row with the lowest PassingLeaderScore for the least frequent PassingLeader from Team1 and Team2
    team1_lowest_score_row = selected_teams_passing_leader_df[
        (selected_teams_passing_leader_df['Team_IN'] == team1) &
        (selected_teams_passing_leader_df['PassingLeader'] == team1_highest_count_leader)].nsmallest(1,
                                                                                                        'PassingLeaderScore')

    team2_lowest_score_row = selected_teams_passing_leader_df[
        (selected_teams_passing_leader_df['Team_IN'] == team2) &
        (selected_teams_passing_leader_df['PassingLeader'] == team2_highest_count_leader)].nsmallest(1,
                                                                                                        'PassingLeaderScore')

    team1_lowest_home_team = team1_lowest_score_row['vs'].values[0]
    team2_lowest_home_team = team2_lowest_score_row['vs'].values[0]
    
    highlight_teams = [team1, team2, team2_highest_home_team, team1_highest_home_team, team2_lowest_home_team,
                       team1_lowest_home_team]
    
    return fig_selected_teams, IntBySchool(team1, team2, team2_highest_home_team, team1_highest_home_team,
                                           team2_lowest_home_team, team1_lowest_home_team), TotPlacement(team1, team2,
                                                                                                        team2_highest_home_team,
                                                                                                        team1_highest_home_team,
                                                                                                        team2_lowest_home_team,
                                                                                                        team1_lowest_home_team), plot_sack_totals_interactive(
        highlight_teams)

