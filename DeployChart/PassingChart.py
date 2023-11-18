from week_finder import *
from IntChart import *
from TotChart import *
from SackChart import *

def PassLeader_Score_Diff(team1,team2):
    start_week = 0
    end_week = get_college_football_week() - 1

    # Create an empty list to store DataFrames for each team
    selected_teams_passing_leader = []

    # Iterate through the specified weeks
    for week in range(start_week, end_week + 1):
        file_path = f'data/week{week}.csv'
        # Load data for the current week with the specified encoding
        current_week_data = pd.read_csv(file_path, encoding='ISO-8859-1')

        # Filter the games involving the selected teams and append to the list
        team1_games = current_week_data[((current_week_data['Away Team'] == team1) | (current_week_data['Home Team'] == team1)) &
                                        ~current_week_data['PassingLeader'].isna()].copy()
        
        team2_games = current_week_data[((current_week_data['Away Team'] == team2) | (current_week_data['Home Team'] == team2)) &
                                        ~current_week_data['PassingLeader'].isna()].copy()

        # Add the week information to the DataFrame
        team1_games['Week'] = team2_games['Week'] = week

        selected_teams_passing_leader.append(team1_games[['Away Team', 'Home Team', 'PassingLeader', 'PassingLeaderScore', 'Week']])
        selected_teams_passing_leader.append(team2_games[['Away Team', 'Home Team', 'PassingLeader', 'PassingLeaderScore', 'Week']])

    # Concatenate all DataFrames to create a single DataFrame for selected teams
    selected_teams_passing_leader_df = pd.concat(selected_teams_passing_leader)

    # Plotting the line chart for PassingLeaderScore over the weeks for selected teams using plotly
    fig_selected_teams = px.line(selected_teams_passing_leader_df, x='Week', y='PassingLeaderScore', color='PassingLeader', markers=True,
                                title=f'PassingLeaderScore Over Weeks for {team1} and {team2}',
                                labels={'PassingLeaderScore': 'PassingLeaderScore', 'Week': 'Week'},
                                hover_data={'Away Team', 'Home Team', 'Week'})

    # Rename the 'Home Team' and 'Away Team' columns to 'vs' and 'Team' respectively
    fig_selected_teams.update_traces(hovertemplate='Week: %{x}<br>Team: %{customdata[1]}<br>vs: %{customdata[0]}<br>PassingLeaderScore: %{y}')

    # Show the plot for PassingLeaderScore over weeks for selected teams with 'vs' and 'Team' in the hover tooltip
    fig_selected_teams.show()
    # Display the interactive plot
    fig_selected_teams.write_html("/ESPN/PassingFig.html")

    
    
    
   # Concatenate all DataFrames to create a single DataFrame for selected teams
    selected_teams_passing_leader_df = pd.concat(selected_teams_passing_leader)

    # Sort the DataFrame by 'PassingLeaderScore' column in ascending order
    selected_teams_passing_leader_df.sort_values(by='PassingLeaderScore', ascending=True, inplace=True)

    # Assuming selected_teams_passing_leader_df is your DataFrame
    leader_counts = selected_teams_passing_leader_df.groupby(['Away Team', 'PassingLeader']).size().reset_index(name='Count')

    # Filter the counts for Team1 and Team2
    team1_counts = leader_counts[leader_counts['Away Team'] == team1]
    team2_counts = leader_counts[leader_counts['Away Team'] == team2]

    # Get the PassingLeader with the highest count for Team1 and Team2
    team1_highest_count_leader = team1_counts.loc[team1_counts['Count'].idxmax(), 'PassingLeader']
    team2_highest_count_leader = team2_counts.loc[team2_counts['Count'].idxmax(), 'PassingLeader']

    # Get the row with the highest PassingLeaderScore for the most frequent PassingLeader from Team1 and Team2
    team1_highest_score_row = selected_teams_passing_leader_df[(selected_teams_passing_leader_df['Away Team'] == team1) &
                                                                (selected_teams_passing_leader_df['PassingLeader'] == team1_highest_count_leader)].nlargest(1, 'PassingLeaderScore')
    team2_highest_score_row = selected_teams_passing_leader_df[(selected_teams_passing_leader_df['Away Team'] == team2) &
                                                                (selected_teams_passing_leader_df['PassingLeader'] == team2_highest_count_leader)].nlargest(1, 'PassingLeaderScore')


    # Extract Home Team names
    team1_highest_home_team = team1_highest_score_row['Home Team'].values[0]
    team2_highest_home_team = team2_highest_score_row['Home Team'].values[0]
    

    # Get the row with the lowest PassingLeaderScore for the least frequent PassingLeader from Team1 and Team2
    team1_lowest_score_row = selected_teams_passing_leader_df[(selected_teams_passing_leader_df['Away Team'] == team1) &
                                                                (selected_teams_passing_leader_df['PassingLeader'] == team1_highest_count_leader)].nsmallest(1, 'PassingLeaderScore')

    team2_lowest_score_row = selected_teams_passing_leader_df[(selected_teams_passing_leader_df['Away Team'] == team2) &
                                                                (selected_teams_passing_leader_df['PassingLeader'] == team2_highest_count_leader)].nsmallest(1, 'PassingLeaderScore')

    team1_lowest_home_team = team1_lowest_score_row['Home Team'].values[0]
    team2_lowest_home_team = team2_lowest_score_row['Home Team'].values[0]

    #print(team1, team2, team2_highest_home_team, team1_highest_home_team, team2_lowest_home_team, team1_lowest_home_team)
    # Call IntBySchool with Home Team names
    IntBySchool(team1, team2, team2_highest_home_team, team1_highest_home_team, team2_lowest_home_team, team1_lowest_home_team)
    # Example usage:

    TotPlacement(team1, team2, team2_highest_home_team, team1_highest_home_team, team2_lowest_home_team, team1_lowest_home_team)
    highlight_teams=[team1, team2, team2_highest_home_team, team1_highest_home_team, team2_lowest_home_team, team1_lowest_home_team]
    plot_sack_totals_interactive( highlight_teams)
    
    return fig_selected_teams, IntBySchool(team1, team2, team2_highest_home_team, team1_highest_home_team, team2_lowest_home_team, team1_lowest_home_team),TotPlacement(team1, team2, team2_highest_home_team, team1_highest_home_team, team2_lowest_home_team, team1_lowest_home_team),plot_sack_totals_interactive( highlight_teams)