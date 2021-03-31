import StockClient
import time
from random import randint
from tkinter import *
import json
import ApiValues

'''
stocks = []

stock = StockClient.get_StockData('https://finance.yahoo.com/quote/TSLA/')
stock1 = StockClient.get_StockData('https://finance.yahoo.com/quote/NVDA?p=NVDA&.tsrc=fin-srch')
stock2 = StockClient.get_StockData('https://finance.yahoo.com/quote/BTC-USD?p=BTC-USD&.tsrc=fin-srch')


'''
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
while i <= 10:
    stock2 = StockClient.get_StockData('https://finance.yahoo.com/quote/BTC-USD?p=BTC-USD&.tsrc=fin-srch')
    if currentStockPrice != stock2.Price:
        print(stock2.Name)
        print(stock2.Price)
    currentStockPrice = stock2.Price
    #seed(1)
    randomNumber = randint(5, 20)
    print("I'm waiting for " + str(randomNumber) + " seconds.")
    time.sleep(randomNumber)
'''
pageUrl = 'https://finance.yahoo.com/quote/BTC-USD?p=BTC-USD&.tsrc=fin-srch'
updateUrl = 'https://query1.finance.yahoo.com/v7/finance/quote?&symbols=BTC-USD&fields=extendedMarketChange,extendedMarketChangePercent,extendedMarketPrice,extendedMarketTime,regularMarketChange,regularMarketChangePercent,regularMarketPrice,regularMarketTime,circulatingSupply,ask,askSize,bid,bidSize,dayHigh,dayLow,regularMarketDayHigh,regularMarketDayLow,regularMarketVolume,volume'

stock2 = StockClient.get_StockUpdate(updateUrl)

print(StockClient.get_Info(stock2, ApiValues.DataType.REGULAR_MARKET_PRICE.value))
print(StockClient.get_StockWebPageData(pageUrl).Name + StockClient.get_StockWebPageData(pageUrl).Price)

'''
json_object = json.loads(stock2)
quoteResponse = json_object["quoteResponse"]
result = quoteResponse["result"]
for item in result[0].items():
    print(item[1])

'''