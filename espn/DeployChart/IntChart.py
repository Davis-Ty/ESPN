#load data
import pandas as pd
import plotly.express as px


def IntBySchool(t1, t2, t3, t4, t5, t6):

    #read data with Pandas from CSV file
    NCAA_df = pd.read_csv("data/defense.csv")

    # Group the data by 'School' and sum the 'INT' column for each group
    school_int_totals = NCAA_df.groupby('School')['INT'].sum().reset_index()

    # Sort the result in descending order by the 'INT' column
    school_int_totals = school_int_totals.sort_values(by='INT', ascending=False)

    # Create a bar chart using Plotly Express
    fig = px.bar(
        school_int_totals,
        x='School',
        y='INT',
        title='Total Interceptions by School',
        labels={'INT': 'Total Interceptions', 'School': 'School'},
        color='INT',  # Color bars based on the number of interceptions
        color_continuous_scale='reds',  # Use a red color scale
        range_color=[school_int_totals['INT'].min(), school_int_totals['INT'].max()],  # Match color scale range to data
    )

    # Customize the layout
    fig.update_layout(
        xaxis_title='School',
        yaxis_title='Total Interceptions',
        coloraxis_colorbar_title='Total Interceptions',
        coloraxis_colorbar_ticks='outside',
        coloraxis_colorbar_tickmode='array',
        coloraxis_colorbar_tickvals=[school_int_totals['INT'].min(), school_int_totals['INT'].max()],
        coloraxis_colorbar_ticktext=['Low', 'High'],
    )

    # Update layout with dotted lines based on user input
    def update_dotted_lines(selected_schools):
        shapes = []
        annotations = []

        for school in selected_schools:
            # Check if the selected school is in the data
            if school in school_int_totals['School'].values:
                color = 'black'  # Use black for existing schools
            else:
                color = 'red'  # Use red for non-existing schools

            shape = {
                'type': 'line',
                'x0': school,
                'x1': school,
                'y0': 0,
                'y1': 1,
                'xref': 'x',
                'yref': 'paper',
                'line': {'dash': 'dash', 'color': color},
            }
            shapes.append(shape)

            annotation = {
                'x': school,
                'y': 1.05,  # Adjust the y-coordinate for the annotation
                'xref': 'x',
                'yref': 'paper',
                'text': school,
                'showarrow': False,
                'font': {'size': 10},
            }
            annotations.append(annotation)

        return shapes, annotations

    # Specify the schools you want lines for
    selected_schools = [t1, t2, t3, t4, t5, t6]  # Replace with your selected schools

    # Add lines and annotations for all selected schools
    shapes, annotations = update_dotted_lines(selected_schools)
    fig.update_layout(shapes=shapes, annotations=annotations)

    # Show the interactive plot
    fig.show()
    # Display the interactive plot
    fig.write_html("/ESPN/IntFig.html")
    return fig