import threading
import StockClient
import time
import ApiValues
from tkinter import *


'''
stocks = []
>>>>>>> parent of abb5dfa (RapidApiFirstIntegration)

stock = StockClient.get_StockData('https://finance.yahoo.com/quote/TSLA/')
stock1 = StockClient.get_StockData('https://finance.yahoo.com/quote/NVDA?p=NVDA&.tsrc=fin-srch')
stock2 = StockClient.get_StockData('https://finance.yahoo.com/quote/BTC-USD?p=BTC-USD&.tsrc=fin-srch')

#Coverting response to json
responseJson = json.loads(response.text)

#responsePython = ResponseMapper.map_response(responseJson)
responsePythonV2 = ResponseMapper.map_responseV2(responseJson)

#print('Assets Company Officers: ' + str(responsePython.AssetProfile.CompanyOfficers))
#print('Assets Name: ' + str(responsePython.AssetProfile.Name))

print('Response V2: ' + str(responsePythonV2.FinancialsTemplate.code))
print('Response V2: ' + str(responsePythonV2.FinancialsTemplate.max_age))

'''

pageUrl = 'https://finance.yahoo.com/quote/BTC-USD?p=BTC-USD&.tsrc=fin-srch'
updateUrl = 'https://query1.finance.yahoo.com/v7/finance/quote?&symbols=BTC-USD&fields=extendedMarketChange,extendedMarketChangePercent,extendedMarketPrice,extendedMarketTime,regularMarketChange,regularMarketChangePercent,regularMarketPrice,regularMarketTime,circulatingSupply,ask,askSize,bid,bidSize,dayHigh,dayLow,regularMarketDayHigh,regularMarketDayLow,regularMarketVolume,volume'

stockWebPage = StockClient.get_StockWebPageData(pageUrl)
stockName = StockClient.get_stockName(stockWebPage)

def start_loop():
    i = 0
    currentStockPrice = None
    while i <= 10:
        updateResponse = StockClient.get_StockUpdate(updateUrl)
        stockPrice = StockClient.get_Info(updateResponse, ApiValues.DataType.REGULAR_MARKET_PRICE.value)

        if currentStockPrice != stockPrice:
            print(stockPrice)
            priceLabel = Label(root, text=stockPrice)
            priceLabel.grid(row=3, column=1)
            #priceLabel.pack()
        currentStockPrice = stockPrice
        time.sleep(3)

def start_thread():
    t1 = threading.Thread(target=start_loop)
    t1.start()

class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()

        self.title("Stock Price Tracker")
        self.minsize(500, 400)

root = Root()

myLabel = Label(root, text=stockName)
myLabel.grid(row=1, column=1)

myButton = Button(root, text="Get Price", command=lambda: start_thread())
myButton.grid(row=2, column=1)

root.mainloop()

