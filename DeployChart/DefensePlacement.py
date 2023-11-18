#load data
import pandas as pd
import plotly.express as px

def TotHist():
    #read data with Pandas from CSV file
    NCAA_df = pd.read_csv("data/defense.csv")
    
    # Group the data by 'School' and sum the 'TOT' column for each group
    school_tot_totals = NCAA_df.groupby('School')['TOT'].sum().reset_index()

    # Sort the result in descending order by the 'TOT' column
    school_tot_totals = school_tot_totals.sort_values(by='TOT', ascending=False)

   
    # Create an interactive distribution plot using Plotly Express
    fig = px.histogram(
        school_tot_totals,
        x='TOT',
        title='Distribution of Total Tackles by School',
        labels={'TOT': 'Total Tackles', 'count': 'Number of Schools'},
        marginal='box',  # Display a box plot on the marginal axis
        opacity=0.7,  # Adjust the opacity of bars
        color_discrete_sequence=['blue'],  # Bar color
        nbins=20  # Adjust the number of bins for a smoother curve
    )

    # Customize the layout
    fig.update_layout(
        xaxis_title='Total Tackles',
        yaxis_title='Number of Schools',
        xaxis=dict(range=[school_tot_totals['TOT'].min(), school_tot_totals['TOT'].max()]),  # Set x-axis range
    )

    # Show the interactive plot
    fig.show()
    # Display the interactive plot and create/override the file
    fig.write_html("/ESPN/TotHistFig.html")
    return fig