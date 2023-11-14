import dash
from dash import dcc, html
from dash.dependencies import Input, Output
from dash_extensions import Slider
import pandas as pd
import plotly.express as px

# Load the data
NCAA_df = pd.read_csv("data/defense.csv")

# Group the data by School and calculate the sum of defensive stats
grouped_data = NCAA_df.groupby('School').sum().reset_index()

# Create a Dash app
app = dash.Dash(__name__)

# Football-themed colors
colors = {
    'background': '#1A5276',
    'text': '#FFD700',
}

# Define the layout of the app
app.layout = html.Div(style={'backgroundColor': colors['background'], 'color': colors['text']}, children=[
    html.H1(children='D3 Football Defensive Stats', style={'textAlign': 'center', 'color': colors['text']}),
    
    # Create a slider and chart pair for each category
    *[html.Div([
        dcc.Graph(
            id=f'football-chart-{col}',
            figure={
                'data': [
                    {'x': grouped_data['School'], 'y': grouped_data[col], 'type': 'bar', 'name': col}
                    for col in grouped_data.columns[2:]  # Exclude 'School' and 'Player' columns
                ],
                'layout': {
                    'title': f'D3 Football Defensive Stats by School ({col})',
                    'barmode': 'stack',
                    'plot_bgcolor': colors['background'],
                    'paper_bgcolor': colors['background'],
                    'font': {'color': colors['text']}
                }
            }
        ),
        Slider(
            id=f'slider-{col}',
            min=0,
            max=100,
            step=1,
            value=50,
            tooltip={"placement": "bottom", "always_visible": True},
        ),
    ]) for col in grouped_data.columns[2:]]
])

# Define callback to update the chart based on slider values
@app.callback(
    [Output(f'football-chart-{col}', 'figure') for col in grouped_data.columns[2:]],
    [Input(f'slider-{col}', 'value') for col in grouped_data.columns[2:]]
)
def update_chart(*slider_values):
    # Create a copy of the original data to modify
    updated_data = grouped_data.copy()

    # Update the values based on slider percentages
    for col, slider_value in zip(grouped_data.columns[2:], slider_values):
        updated_data[col] = updated_data[col] * (slider_value / 100)

    # Sort the dataframe based on the selected category
    selected_category = grouped_data.columns[2:][slider_values.index(max(slider_values))]
    updated_data = updated_data.sort_values(by=selected_category, ascending=False)

    # Return the updated charts
    return [
        {
            'data': [
                {'x': updated_data['School'], 'y': updated_data[col], 'type': 'bar', 'name': col}
                for col in updated_data.columns[2:]  # Exclude 'School' and 'Player' columns
            ],
            'layout': {
                'title': f'D3 Football Defensive Stats by School ({col})',
                'barmode': 'stack',
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {'color': colors['text']}
            }
        }
        for col in updated_data.columns[2:]
    ]

# Save the layout as an HTML file
with open("football_dashboard.html", "w") as file:
    file.write(html.Div(children=app.layout).to_html())

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
