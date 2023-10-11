from matplotlib import pyplot as plt
from week_finder import *
import json

def passing_ml(get_college_football_week,players,schools,grouped_stats_dict,name,name2, name3):
        per_game_averages = {
        'ATT': 0,
        'YDS': 0,
        'TD': 0,
        'INT': 0,
        'SACK': 0
    }
        i=-1
        
        
    # Iterate through each name in the list
        for player in players:
            i=i+1
            if player == name or  player == name2 or player == name3:
                print("")
                print(f"Player: {player}")
                
                
                print(f"school: {schools[i]}")
                # add code to return the team this school will be playing
                #add code to return (show) the avagerage stats of the defense compared to other teams
                #^ that code should show if they are playing a below avg/avg/above avg defense 
                

                # Iterate through each key-value pair in the dictionary
                for key, value in grouped_stats_dict.items():
                    if key == 'POS':
                        print(f"  {key}: {value[i]} ")
                    elif key in ['ATT', 'YDS', 'TD', 'INT', 'SACK']:
                        #print(f"  {key}: {value[i] } ")
                        
                        num=json.dumps(value[i])
                        num=int(num.strip('[]""').replace(',', ''))
                        
                        per_game_avg=num/get_college_football_week
                        print(f"{key} per game avg: {per_game_avg}")
                        per_game_averages[key] = per_game_avg
                    elif key == 'RTG':
                        print(f"  {key}: {value[i]} ")
                        
                # Create a bar chart for the per-game averages
                #this will be changed
                plt.bar(per_game_averages.keys(), per_game_averages.values())
                plt.xlabel('Statistic')
                plt.ylabel('Per Game Average')
                plt.title('Per Game Averages for Football Statistics')
                plt.show()
                
                #add code to (show) what the prediction for passing yards will be based off of the defense that will be played against 