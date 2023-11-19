#load data
import pandas as pd
import plotly.express as px


def plot_sack_totals_interactive(highlight_teams):
    """
    Plot the total number of sacks by school in an interactive bar chart.

    Parameters:
    - school_sack_totals: DataFrame with 'School' and 'SACK' columns.
    - highlight_teams: List of teams to highlight in the chart.

    Returns:
    - None (displays the interactive plot).
    
    """
    #read data with Pandas from CSV file
    NCAA_df = pd.read_csv("data/defense.csv")

    # Group the data by 'School' and sum the 'TOT' column for each group
    school_sack_totals = NCAA_df.groupby('School')['SACK'].sum().reset_index()

    # Sort the result in descending order by the 'TOT' column
    school_sack_totals = school_sack_totals.sort_values(by='SACK', ascending=False)

    # Assign colors based on the position in the highlight_teams list
    color_mapping = {'blue': 'Non Included teams','purple':'selected teams', 'green': 'Bad Team', 'red': 'Good Team'}
    school_sack_totals['Color'] = school_sack_totals['School'].apply(lambda x: color_mapping.get(
        'green') if x == highlight_teams[0] or x == highlight_teams[1] else (
            color_mapping.get('red') if x == highlight_teams[2] or x == highlight_teams[3] else
            color_mapping.get('purple')))

    # Create an interactive bar chart using plotly express
    fig = px.bar(
        school_sack_totals,
        x='School',
        y='SACK',
        color='Color',
        labels={'SACK': 'Total Sacks'},
        title='Total Number of Sacks by School',
        text='SACK',  # Display the sack totals on top of bars
    )

    # Customize the layout for better readability
    fig.update_layout(
        xaxis_title='School',
        yaxis_title='Total Sacks',
        xaxis=dict(tickangle=45),
    )

    # Display the interactive plot
    fig.show()
    # Display the interactive plot
    fig.write_html("/ESPN/SackFig.html")

    return fig

