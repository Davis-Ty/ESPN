#load data
import pandas as pd
import plotly.express as px

def TotPlacement(t1, t2, t3, t4, t5, t6):

    """
    Create an interactive distribution plot of total tackles for selected schools.

    Parameters:
    - school_tot_totals: DataFrame with 'School' and 'TOT' columns.
    - t1, t2, t3, t4, t5, t6: Names of schools to highlight.

    Returns:
    - None (displays the interactive plot).
    """
    #read data with Pandas from CSV file
    NCAA_df = pd.read_csv("data/defense.csv")
    # Group the data by 'School' and sum the 'TOT' column for each group
    school_tot_totals = NCAA_df.groupby('School')['TOT'].sum().reset_index()

    # Sort the result in descending order by the 'TOT' column
    school_tot_totals = school_tot_totals.sort_values(by='TOT', ascending=False)

    # Create a distribution plot using Plotly Express
    fig = px.histogram(
        school_tot_totals,
        x='TOT',
        marginal='rug',  # Add rug plot for individual data points
        color_discrete_sequence=['orange'],  # Set the color for the histogram bars
        labels={'TOT': 'Total Tackles'},
        title='Distribution of Total Tackles for All Schools',
        nbins=30,  # Number of bins for the histogram
    )

    # Add vertical lines and annotations for each team's total tackles
    team_colors = {'steelblue': t1, 'lightblue': t2, 'forestgreen': t3, 'limegreen': t4, 'darkred': t5, 'firebrick': t6}

    for color, team in team_colors.items():
            if team in school_tot_totals['School'].values:
                total_tackles = school_tot_totals.loc[school_tot_totals['School'] == team, 'TOT'].values[0]
                fig.add_shape(
                    type='line',
                    x0=total_tackles,
                    x1=total_tackles,
                    y0=0,
                    y1=0.8,
                    xref='x',
                    yref='paper',
                    line=dict(color=color, dash='dash'),
                )
                
                # Add annotation for the school name
                fig.add_annotation(
                    x=total_tackles,
                    y=1.05,  # Adjust the y-coordinate for the annotation
                    xref='x',
                    yref='paper',
                    text=team,
                    showarrow=False,
                    font=dict(size=10),
                )

    # Add hover text for each school
    fig.update_traces(hovertext=school_tot_totals['School'])

    # Customize the layout
    fig.update_layout(
        xaxis_title='Total Tackles',
        yaxis_title='Density',
        showlegend=False,  # Do not show legend for histogram bars
    )

    # Display the interactive plot
    fig.show()
    # Display the interactive plot
    fig.write_html("/ESPN/TotFig.html")
    return fig