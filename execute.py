import marketSummary as m1
import todayShare as m2


for i in range(0, len(m1.header)):
    m1.marketSummaryScrape(m1.listOfIndex[i], m1.header[i])

m2.todayMarketScrape()