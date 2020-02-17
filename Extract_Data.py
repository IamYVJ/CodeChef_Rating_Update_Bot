from bs4 import BeautifulSoup

def getData(rawSource):
    soup = BeautifulSoup(rawSource, 'html5lib')
    ratings = []
    for row in soup.findAll('div', attrs = {'class':'rating-number'}):
        ratings.append(str(row.text))
    return ratings
