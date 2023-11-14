def get_url():
    passing_url = 'https://www.espn.com/college-football/stats/player'
    
    rushing_url= 'https://www.espn.com/college-football/stats/player/_/view/offense/stat/rushing/table/rushing/sort/rushingYards/dir/desc'
    
    receiving_url='https://www.espn.com/college-football/stats/player/_/view/offense/stat/receiving/table/receiving/sort/receivingYards/dir/desc'
    
    defense_url='https://www.espn.com/college-football/stats/player/_/view/defense'
    
    
    
    urls=[passing_url,
    rushing_url,receiving_url,defense_url]
    
    return urls