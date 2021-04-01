from Yahoo import YahooRequest
from Yahoo import YahooResponse
from Yahoo import YahooSubmitter
import json

querystring = {"symbol":"BTC-USD","region":"US"}
request = YahooRequest.YahooRequest("BTC-USD", "US")

response = YahooSubmitter.submit(request)

#Coverting response to json
responseJson = json.loads(response.text)

#Initializing a YahooResponse object
responsePython = YahooResponse

#Mapping data
responsePython.YahooResponse.FinancialsTemplate = responseJson["financialsTemplate"]

price = responseJson["price"]
responsePython.Price.QuoteSourceName = price["quoteSourceName"]

regularMarketOpen = price["regularMarketOpen"]
responsePython.Price.RegularMarketOpen = YahooResponse.RegularMarketOpen(regularMarketOpen["raw"], regularMarketOpen["fmt"])

averageDailyVolume3Month = price["averageDailyVolume3Month"]
responsePython.Price.AverageDailyVolume3Month = YahooResponse.AverageDailyVolume3Month(averageDailyVolume3Month["raw"], averageDailyVolume3Month["fmt"], averageDailyVolume3Month["longFmt"])


print('Average Daily Volume 3 Month')
print(responsePython.Price.AverageDailyVolume3Month.raw)
print(responsePython.Price.AverageDailyVolume3Month.fmt)
print(responsePython.Price.AverageDailyVolume3Month.longFmt)