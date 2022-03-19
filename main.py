import threading
import StockClient
import time
import ApiValues
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget
import sys

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
        currentStockPrice = stockPrice
        time.sleep(3)

def start_thread():
    t1 = threading.Thread(target=start_loop)
    t1.start()


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()

        self.label = QLabel("My text")
        self.layout.addWidget(self.label)

        self.setGeometry(300, 300, 600, 400)
        self.setLayout(self.layout)
        self.setWindowTitle("Stock Price Tracker")
        #self.show()


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
