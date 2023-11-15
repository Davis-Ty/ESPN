import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Assume you have the required functions (IntBySchool, TotPlacement, plot_sack_totals_interactive) defined

# Load the data
NCAA_df = pd.read_csv("/espn/data/defense.csv")

# Create a Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    dcc.Dropdown(
        id='team-dropdown-1',
        options=[{'label': team, 'value': team} for team in NCAA_df['Away Team'].unique()],
        value='TeamA',
        style={'width': '50%', 'margin': '20px auto'},
    ),
    dcc.Dropdown(
        id='team-dropdown-2',
        options=[{'label': team, 'value': team} for team in NCAA_df['Away Team'].unique()],
        value='TeamB',
        style={'width': '50%', 'margin': '20px auto'},
    ),
    dcc.Graph(id='interactive-chart')
])

# Define callback to update the chart based on selected teams
@app.callback(
    Output('interactive-chart', 'figure'),
    [Input('team-dropdown-1', 'value'),
     Input('team-dropdown-2', 'value')]
)
def update_chart(team1, team2):
    # Your logic for updating the chart goes here
    # Call the required functions based on selected teams

    # Example usage:
    TotPlacement(team1, team2, ...)
    highlight_teams = [team1, team2, ...]

    # Assuming you want to create a bar chart of PassingLeaderScore
    fig = px.bar(NCAA_df, x='Week', y='PassingLeaderScore', color='PassingLeader',
                 labels={'PassingLeaderScore': 'PassingLeaderScore', 'Week': 'Week'},
                 hover_data={'Away Team', 'Home Team', 'Week'},
                 title=f'PassingLeaderScore Over Weeks for {team1} and {team2}')

    # Show the plot
    fig.show()

    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
