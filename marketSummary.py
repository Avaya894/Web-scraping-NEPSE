#Top Gainers, Top Losers, Top Traded Shares

from bs4 import BeautifulSoup
import requests
import lxml
import pandas as pd

# Site URL
url = "https://www.sharesansar.com/market"
con = requests.get(url)
soup = BeautifulSoup(con.text, 'lxml')  # code of the page

#Heading
header = ['Index','SubIndex', 'TopGainers', 'TopTurnOvers', 'TopLosers', 'TopTradedShares']
listOfIndex = [0, 3, 6, 7, 8, 9]

def marketSummaryScrape(index, header):
    table = soup.find_all('table', class_="table table-bordered table-striped table-hover")[index] 
    listOfHeading = [i.text for i in table.find_all('th')]  # data of the th tag

    rows = table.find_all('tr')
    data = []
    for element in rows[1:]:
        body = element.find_all('td')
        list = []
        list = [i.text for i in body]
        data.append(list)

    df = pd.DataFrame(data, columns = listOfHeading)

    # Filtering
    # Removing comma
    for each in listOfHeading:
        df[each] = df[each].str.replace('\n', '')
        df[each] = df[each].str.replace(',', '')
        df[each] = df[each].str.strip()

    df.set_index(listOfHeading[0], inplace = True)

    df.to_csv(f'{header}.csv')