import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import random
from dash import html
from DefensePlacement import *
from PassingChart import *
from RunningChart import *
from ScoreChart import *
from dash.dependencies import Input, Output, State

# Load the data
NCAA_df = pd.read_csv("/espn/data/defense.csv")

# Group the data by School and calculate the sum of defensive stats
grouped_data = NCAA_df.groupby('School').sum().reset_index()

# Add a symbol column with a football emoji for each school
grouped_data['symbol'] = '🏈'  # You can replace this with the emoji or symbol you prefer

# Generate random colors for each category
category_colors = {
    stat: f'rgb({random.randint(0, 255)}, {random.randint(0, 255)}, {random.randint(0, 255)})' 
    for stat in ['SOLO', 'AST', 'TOT', 'SACK', 'YDS', 'PD', 'INT', 'LNG', 'TD', 'FF']
}

# Generate random colors for each school
grouped_data['Color'] = ['#%02X%02X%02X' % (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) 
                         for _ in range(len(grouped_data))]

# Create a Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Football-themed colors
colors = {
    'text': '#FFD700',
}

# Create the HTML div elements for the additional charts
app.layout = html.Div(style={'backgroundColor': 'black', 'color': colors['text']}, children=[
    dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("About", href="https://davis-ty.github.io/ESPN/")),
            dbc.NavItem(dbc.NavLink("Contact", href="https://davis-ty.github.io/repository/")),
        ],
        brand="Football Defensive Stats",
        brand_href="#",
        color="primary",
        dark=True,
    ),
    html.H1(children='2023 Football Defensive Stats', style={'textAlign': 'center', 'color': 'yellow'}),

    dcc.Graph(
        id='allD-chart',
    ),
    html.Div([
        dcc.Dropdown(
            id='stat-dropdown',
            options=[
                {'label': 'Solo Tackles', 'value': 'SOLO'},
                {'label': 'Assist Tackles', 'value': 'AST'},
                {'label': 'Total Tackles', 'value': 'TOT'},
                {'label': 'Sacks', 'value': 'SACK'},
                {'label': 'Yards Lost', 'value': 'YDS'},
                {'label': 'Passes Defended', 'value': 'PD'},
                {'label': 'Interceptions', 'value': 'INT'},
                {'label': 'Touchdowns', 'value': 'TD'},
                {'label': 'Forced Fumbles', 'value': 'FF'},
            ],
            value='SOLO',
            style={'width': '50%', 'margin': '20px auto', 'backgroundColor': 'black', 'color': 'black'},
        ),
        dcc.Slider(
            id='scale-slider',
            min=0,
            max=grouped_data['SOLO'].max(),
            step=1,
            value=grouped_data['SOLO'].max() // 2,
            marks={i: f'{i}%' for i in range(0, 101, 10)},
            tooltip={"placement": "bottom", "always_visible": True},
        ),
    ], style={'margin': '20px', 'color': 'yellow', 'backgroundColor': 'black'}),

    dcc.Graph(
        id='football-chart',
    ),
    html.Div([
        dcc.Dropdown(
            id='team-dropdown-1',
            options=[{'label': team, 'value': team} for team in grouped_data['School']],
            value='TeamA',
            style={'width': '50%', 'margin': '20px auto', 'color': 'black', 'backgroundColor': 'black'},
        ),
        dcc.Dropdown(
            id='team-dropdown-2',
            options=[{'label': team, 'value': team} for team in grouped_data['School']],
            value='TeamB',
            style={'width': '50%', 'margin': '20px auto', 'color': 'black', 'backgroundColor': 'black'},
        ),
    ], style={'margin': '20px'}),

    dcc.Graph(
        id='radar-chart',
        style={'backgroundColor': 'green'},  # Set background color of the radar chart
    ),

    # Additional HTML charts (initially hidden)
    html.Div(id='int-chart', style={'display': 'none'}),
    html.Div(id='passing-chart', style={'display': 'none'}),
    html.Div(id='running-chart', style={'display': 'none'}),
    html.Div(id='sack-chart', style={'display': 'none'}),
    html.Div(id='score-chart', style={'display': 'none'}),
    html.Div(id='tot-chart', style={'display': 'none'}),
    html.Div(id='tot-hist-chart', style={'display': 'none'}),
])

# Define callback to update the chart based on dropdown and slider interactions
@app.callback(
    Output('allD-chart', 'figure'),
    [Input('allD-chart', 'relayoutData')]
)
def update_chart(relayoutData):
    selected_stats = ['SOLO', 'AST', 'TOT', 'SACK', 'YDS', 'PD', 'INT', 'LNG', 'TD', 'FF']

    # Create a copy of the original data to modify
    updated_data = grouped_data.copy()

    # Remove categories based on user interaction
    if relayoutData is not None and 'xaxis.range[0]' in relayoutData:
        min_val, max_val = relayoutData['xaxis.range[0]'], relayoutData['xaxis.range[1]']
        selected_stats = [stat for stat in selected_stats if min_val <= updated_data[stat].sum() <= max_val]

    # Set the values of teams below the threshold to zero
    updated_data[selected_stats] = updated_data[selected_stats].where(updated_data[selected_stats] > 0, 0)

    # Sort the data by the sum of selected categories in descending order
    updated_data = updated_data.sort_values(by=selected_stats, ascending=[False] * len(selected_stats))

    # Create a stacked bar chart with each category having its own color
    fig = go.Figure()

    for stat in selected_stats:
        fig.add_trace(go.Bar(
            x=updated_data['School'],
            y=updated_data[stat],
            name=stat,
            marker=dict(color=category_colors[stat]),
        ))

    # Customize the layout
    fig.update_layout(
        barmode='stack',
        plot_bgcolor='darkgreen',  # Set the background color to green for a football field
        paper_bgcolor='rgba(0, 0, 0, 0)',  # Make the paper background transparent
        font_color=colors['text'],
        xaxis=dict(title='School', showgrid=False, zeroline=False),
        yaxis=dict(title='Stats', showgrid=False, zeroline=False),
    )

    return fig

# Define callback to update the radar chart based on selected teams
@app.callback(
    Output('radar-chart', 'figure'),
    [Input('team-dropdown-1', 'value'),
     Input('team-dropdown-2', 'value'),
     ]
)
def update_radar_chart(team1, team2):

    # Extract data for the selected teams
    selected_teams = grouped_data[grouped_data['School'].isin([team1, team2])]

    # Create radar chart
    fig = go.Figure()

    for i, team in selected_teams.iterrows():
        fig.add_trace(go.Scatterpolar(
            r=team[['SOLO', 'AST', 'TOT', 'SACK', 'YDS', 'PD', 'INT', 'TD', 'FF']].tolist() + [team['SOLO']],
            theta=['SOLO', 'AST', 'TOT', 'SACK', 'YDS', 'PD', 'INT', 'TD', 'FF', 'SOLO'],
            fill='toself',
            name=team['School'],
            line=dict(color=team['Color']),
            marker=dict(symbol='circle', size=8),
            textfont=dict(color='yellow')  # Set text color to yellow
        ))

    # Trigger the update_additional_charts callback
    return fig

# Define callback to update and show the additional HTML charts
@app.callback(
    [Output('int-chart', 'children'),
     Output('passing-chart', 'children'),
     Output('running-chart', 'children'),
     Output('sack-chart', 'children'),
     Output('score-chart', 'children'),
     Output('tot-chart', 'children'),
     Output('tot-hist-chart', 'children')],
    [Input('team-dropdown-1', 'value'),
     Input('team-dropdown-2', 'value')]
)
def update_additional_charts(team1, team2):
    # Check if both teams are filled
    if team1 == 'TeamA' or team2 == 'TeamB':
        raise dash.exceptions.PreventUpdate

    # Assuming you have file paths to your HTML files
    passing_content, sack_content, int_content, tot_content = PassLeader_Score_Diff(team1, team2)
    running_content = RushLeader_Score_Diff(team1, team2)
    score_content = Score_Diff(team1, team2)
    tot_hist_content = TotHist()

    return int_content, passing_content, running_content, sack_content, score_content, tot_content, tot_hist_content

# Define callback to update the slider properties based on the selected defensive category
@app.callback(
    [Output('scale-slider', 'max'),
     Output('scale-slider', 'value')],
    [Input('stat-dropdown', 'value')]
)
def update_slider(selected_stat):
    max_value = grouped_data[selected_stat].max()
    default_value = max_value // 2
    return max_value, default_value

# Define callback to update the chart based on dropdown and slider interactions
@app.callback(
    Output('football-chart', 'figure'),
    [Input('stat-dropdown', 'value'),
     Input('scale-slider', 'value')]
)
def update_chart(selected_stat, scale_value):
    # Create a copy of the original data to modify
    updated_data = grouped_data.copy()

    # Set the values of teams below the threshold to zero
    updated_data[selected_stat] = updated_data[selected_stat].where(updated_data[selected_stat] >= scale_value, 0)

    # Sort the data by the selected category in descending order
    updated_data = updated_data.sort_values(by=selected_stat, ascending=False)

    # Use Plotly Express to create the scatter chart with football symbols
    fig = go.Figure()

    for i, row in updated_data.iterrows():
        # Determine the circle color based on the school's assigned color
        circle_color = row['Color']

        # Determine the border color based on whether the school meets the selected limit
        border_color = 'green' if row[selected_stat] >= scale_value else 'white'

        # Add a circle for each school with a different color background
        fig.add_trace(go.Scatter(
            x=[row['School']],
            y=[row[selected_stat]],
            mode='markers',
            marker=dict(
                symbol='circle',
                color=circle_color,
                size=row[selected_stat] * 0.05,
                line=dict(color=border_color, width=2),
            ),
            showlegend=False,
        ))

        # Add a football symbol on top of each circle
        fig.add_trace(go.Scatter(
            x=[row['School']],
            y=[row[selected_stat]],
            mode='text',
            text='🏈',
            textfont=dict(size=14, color='yellow'),  # Set text color to yellow
            showlegend=False,
        ))

    # Customize the layout to resemble a football field
    fig.update_layout(
        plot_bgcolor='darkgreen',  # Set the background color to green for a football field
        paper_bgcolor='rgba(0, 0, 0, 0)',  # Make the paper background transparent
        font_color=colors['text'],
        title=f'American College Football Defensive Stats by School ({selected_stat})',
        xaxis=dict(title='School', showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(title=selected_stat, showgrid=False, zeroline=False),
    )

    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
