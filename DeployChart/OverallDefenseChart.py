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

# Generate random colors for each school
grouped_data['Color'] = ['#%02X%02X%02X' % (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in range(len(grouped_data))]

# Create a Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Football-themed colors
colors = {
    'text': '#FFD700',
}

app.layout = html.Div(style={'backgroundImage': 'url("/espn/Football.jpg")', 'backgroundColor': 'black', 'backgroundSize': 'cover', 'color': colors['text']}, children=[


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
            style={'width': '50%', 'margin': '20px auto', 'backgroundColor': 'black', 'color': 'Blacl'},
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
    ], style={'margin': '20px','color':'blue','backgroundColor': 'black'}),

    dcc.Graph(
        id='football-chart',
    )
])

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
            textfont=dict(size=14),
            showlegend=False,
        ))

    # Customize the layout to resemble a football field
    fig.update_layout(
        plot_bgcolor='darkgreen',  # Set the background color to green for a football field
        paper_bgcolor='rgba(0, 0, 0, 0)',  # Make the paper background transparent
        font_color=colors['text'],
        title=f'American Football Defensive Stats by School ({selected_stat})',
        xaxis=dict(title='School', showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(title=selected_stat, showgrid=False, zeroline=False),
    )

    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True, port=8050)

    # Save the app to an HTML file
    app.write_html("FootballDash.html")