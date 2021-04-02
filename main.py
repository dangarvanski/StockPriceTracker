from Yahoo import YahooRequest
from Yahoo import YahooSubmitter
from Yahoo.Mappers import ResponseMapper
import json

querystring = {"symbol":"BTC-USD","region":"US"}
request = YahooRequest.YahooRequest("BTC-USD", "US")

response = YahooSubmitter.submit(request)

#Coverting response to json
responseJson = json.loads(response.text)

responsePython = ResponseMapper.map_response(responseJson)

print('Average Daily Volume 3 Month')
print('Raw: ' + str(responsePython.Price.AverageDailyVolume3Month.raw))
print('Fmt: ' + str(responsePython.Price.AverageDailyVolume3Month.fmt))
print('Long Fmt: ' + str(responsePython.Price.AverageDailyVolume3Month.longFmt))

print('Exchange: ' + responsePython.Price.Exchange)
print('Short name: ' + responsePython.Price.ShortName)