import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import random

# Load the data
NCAA_df = pd.read_csv("/espn/data/defense.csv")

# Group the data by School and calculate the sum of defensive stats
grouped_data = NCAA_df.groupby('School').sum().reset_index()

# Add a symbol column with a football emoji for each school
grouped_data['symbol'] = '🏈'  # You can replace this with the emoji or symbol you prefer

# Generate random colors for each category
category_colors = {stat: f'rgb({random.randint(0, 255)}, {random.randint(0, 255)}, {random.randint(0, 255)})' for stat in ['SOLO', 'AST', 'TOT', 'SACK', 'YDS', 'PD', 'INT', 'LNG', 'TD', 'FF']}

# Create a Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Football-themed colors
colors = {'text': '#FFD700'}

app.layout = html.Div(style={'backgroundColor': 'black', 'backgroundSize': 'cover', 'color': colors['text']}, children=[

    dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("About", href="#")),
            dbc.NavItem(dbc.NavLink("Contact", href="#")),
        ],
        brand="Football Defensive Stats",
        brand_href="#",
        color="primary",
        dark=True,
    ),
    html.H1(children='Football Defensive Stats', style={'textAlign': 'center', 'color': colors['text']}),

    dcc.Graph(
        id='football-chart',
    )
])

# Define callback to update the chart based on dropdown and slider interactions
@app.callback(
    Output('football-chart', 'figure'),
    [Input('football-chart', 'relayoutData')]
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

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True, port=8050)