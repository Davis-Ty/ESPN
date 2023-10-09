from bs4 import BeautifulSoup

def scrape_header(driver):
    headers = BeautifulSoup(driver.page_source, 'lxml')
    header = headers.find(class_='Table__Scroller')
    tags = header.find_all('a')
    stat_header = [g.get_text() for g in tags]
    stat_header.insert(0, 'POS')
    return stat_header
