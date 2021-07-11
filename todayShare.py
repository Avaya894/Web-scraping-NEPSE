#Today's Share Price

from bs4 import BeautifulSoup
import requests
import lxml
import pandas as pd


def todayMarketScrape():
    url1 = "https://www.sharesansar.com/today-share-price"
    con1 = requests.get(url1).text
    soup1 = BeautifulSoup(con1, 'lxml')


    table = soup1.find('table')
    data = []
    row = table.tbody.find_all('tr')

    data = []
    heading = table.find('thead').find_all('th')

    #For List Of Heading
    listOfHeading = []
    for each in heading:
        listOfHeading.append(each.text)


    #For List of table data
    for element in row:
        body = element.find_all('td')
        list = []
        list = [i.text for i in body]
        data.append(list)

    df = pd.DataFrame(data, columns = listOfHeading)

    # Filtering
    # Removing comma
    for each in listOfHeading:
        df[each] = df[each].str.replace(',', '')
        df[each] = df[each].str.replace('\n', '')

    hypenenList = ['120 Days', '180 Days', ]
    for each in hypenenList:
        df[each] = df[each].str.replace('-', '0')
        
    # Converting string to float
    for each in listOfHeading[3:21]:
        df[each].astype(float)


    #Setting Index Value
    listOfHeading[1:]
    df = df[listOfHeading[1:]]
    df.set_index(listOfHeading[1], inplace = True)

    df.to_csv('Todayscrape.csv')
