import csv

def UpdateWeekCSV(list_of_dicts, csv_file_path):
    if not list_of_dicts:
        return  # Handle an empty list of dictionaries

    # Create a list of fieldnames for the CSV file
    fieldnames = list(list_of_dicts[0].keys())

    # Create a list of rows to be written to the CSV file
    csv_data = []

    for dict_item in list_of_dicts:
        # Create a dictionary for the current row
        row = {key: dict_item.get(key, '') for key in fieldnames}
        csv_data.append(row)

    # Write the data to the CSV file
    with open(csv_file_path, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(csv_data)
