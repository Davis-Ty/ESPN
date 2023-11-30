# Load necessary libraries
import pandas as pd
import plotly.express as px

def plot_sack_totals_interactive(highlight_teams):
    """
    Plot the total number of sacks by school in an interactive bar chart.

    Parameters:
    - highlight_teams: List of teams to highlight in the chart.

    Returns:
    - None (displays the interactive plot).
    """
    # Read data with Pandas from CSV file
    NCAA_df = pd.read_csv("data/defense.csv")

    # Group the data by 'School' and sum the 'SACK' column for each group
    school_sack_totals = NCAA_df.groupby('School')['SACK'].sum().reset_index()

    # Sort the result in descending order by the 'SACK' column
    school_sack_totals = school_sack_totals.sort_values(by='SACK', ascending=False)

    # Assign colors and labels based on the position in the highlight_teams list
    color_mapping = {
        highlight_teams[0]: {'color': 'blue', 'label': 'Selected Team'},
        highlight_teams[1]: {'color': 'blue', 'label': 'Selected Team'},
        highlight_teams[2]: {'color': 'red', 'label': 'Bad Game'},
        highlight_teams[3]: {'color': 'red', 'label': 'Bad Game'},
        highlight_teams[4]: {'color': 'green', 'label': 'Good Game'},
        highlight_teams[5]: {'color': 'green', 'label': 'Good Game'}
    }

    # Map the colors to the 'School' column with a default color for missing keys
    school_sack_totals['Color'] = school_sack_totals['School'].map(lambda x: color_mapping.get(x, {'color': 'gray'})['color'])

    # Map the labels to the 'School' column
    school_sack_totals['Label'] = school_sack_totals['School'].map(lambda x: color_mapping.get(x, {'label': 'Other'})['label'])

    # Create an interactive bar chart using Plotly Express
    fig = px.bar(
        school_sack_totals,
        x='School',
        y='SACK',
        color='Color',
        text='Label',  # Display the labels on top of bars
        labels={'SACK': 'Total Sacks'},
        title='Total Number of Sacks by School',
    )

    # Customize the layout for better readability
    fig.update_layout(
        xaxis_title='School',
        yaxis_title='Total Sacks',
        xaxis=dict(tickangle=45),
    )

    # Display the interactive plot
    fig.show()
    
    # Save the interactive plot as an HTML file
    fig.write_html("/ESPN/SackFig.html")

    return fig



