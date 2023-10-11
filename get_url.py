def get_url():
    passing_url = 'https://www.espn.com/college-football/stats/player'
    
    rushing_url= 'https://www.espn.com/college-football/stats/player/_/view/offense/stat/rushing/table/rushing/sort/rushingYards/dir/desc'
    
    receiving_url='https://www.espn.com/college-football/stats/player/_/view/offense/stat/receiving/table/receiving/sort/receivingYards/dir/desc'
    
    defense_url='https://www.espn.com/college-football/stats/player/_/view/defense'
    
    special_return_url='https://www.espn.com/college-football/stats/player/_/view/special'
    
    kick_url='https://www.espn.com/college-football/stats/player/_/view/special/stat/kicking'
    
    punting_url='https://www.espn.com/college-football/stats/player/_/view/special/stat/punting'
    
    scoring_url='https://www.espn.com/college-football/stats/player/_/view/scoring'
    
    
    urls=[passing_url,
    rushing_url,receiving_url,defense_url,special_return_url,kick_url, punting_url,scoring_url]
    
    return urls