import csv

def UpdateCSV(players, schools, grouped_stats_dict, csv_file_path):
    # Create a list to store the data that will be written to the CSV file
    csv_data = []

    if len(players) > 1:
        # Iterate through each name in the list
        for i, player in enumerate(players):
            # Remove square brackets, double quotation marks, and spaces from the player name
            player = player.replace('[', '').replace(']', '').replace('"', '')
            # Remove square brackets, double quotation marks, and spaces from the school name
            school = schools[i].replace('[', '').replace(']', '').replace('"', '').replace("'",'')
            row = {
                "Player": player,
                "School": school
            }

            # Iterate through each key-value pair in the dictionary
            for key, value in grouped_stats_dict.items():
                # Remove square brackets, double quotation marks, and spaces from the values
                cleaned_value = str(value[i]).replace('[', '').replace(']', '').replace('"', '').replace(' ', '').replace("'",'').replace(",",'')
                row[key] = cleaned_value

            csv_data.append(row)

        # Write the data to a CSV file
        with open(csv_file_path, 'w', newline='') as csv_file:
            fieldnames = ["Player", "School"] + list(grouped_stats_dict.keys())
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for row in csv_data:
                writer.writerow(row)
