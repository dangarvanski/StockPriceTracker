import StockClient
import time
import ApiValues
from tkinter import *

'''
stocks = []

stock = StockClient.get_StockData('https://finance.yahoo.com/quote/TSLA/')
stock1 = StockClient.get_StockData('https://finance.yahoo.com/quote/NVDA?p=NVDA&.tsrc=fin-srch')
stock2 = StockClient.get_StockData('https://finance.yahoo.com/quote/BTC-USD?p=BTC-USD&.tsrc=fin-srch')


'''

class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()

        self.title("Python Tkinter")
        self.minsize(500, 400)


root = Root()
root.mainloop()

i = 0
currentStockPrice = None
pageUrl = 'https://finance.yahoo.com/quote/BTC-USD?p=BTC-USD&.tsrc=fin-srch'
updateUrl = 'https://query1.finance.yahoo.com/v7/finance/quote?&symbols=BTC-USD&fields=extendedMarketChange,extendedMarketChangePercent,extendedMarketPrice,extendedMarketTime,regularMarketChange,regularMarketChangePercent,regularMarketPrice,regularMarketTime,circulatingSupply,ask,askSize,bid,bidSize,dayHigh,dayLow,regularMarketDayHigh,regularMarketDayLow,regularMarketVolume,volume'

stockWebPage = StockClient.get_StockWebPageData(pageUrl)
print(StockClient.get_stockName(stockWebPage))
print('Current Price: ')
while i <= 10:
    updateResponse = StockClient.get_StockUpdate(updateUrl)
    stockPrice = StockClient.get_Info(updateResponse, ApiValues.DataType.REGULAR_MARKET_PRICE.value)

    if currentStockPrice != stockPrice:
        print(stockPrice)
    currentStockPrice = stockPrice
    time.sleep(3)