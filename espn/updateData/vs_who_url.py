import datetime 

def vs_who_url():
    today= datetime.date.today()
    year=today.year
    
    vs_urls=[]
    
    for j in range (1,15):
        vs_urls.append(f"https://www.espn.com/college-football/schedule/_/week/{j}/year/{year}/seasontype/2")
        
    for j in range (3,4):
        vs_urls.append(f"https://www.espn.com/college-football/schedule/_/week/1/year/{year}/seasontype/{j}")
 
    return vs_urls