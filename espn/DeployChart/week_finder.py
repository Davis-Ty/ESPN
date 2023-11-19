from datetime import datetime, timedelta

def get_college_football_week():
    # Define the start date of the college football season
    start_date = datetime(2023, 8, 26) 

    # Get the current date
    current_date = datetime.today()

    # Calculate the difference in days from the start date
    days_difference = (current_date - start_date).days

    # Calculate the week based on a 7-day week
    college_football_week = (days_difference // 7) + 1
    
    if college_football_week>16:
        college_football_week=16
        

    return college_football_week-1
