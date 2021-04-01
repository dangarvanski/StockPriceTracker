from Yahoo import YahooRequest
from Yahoo import YahooSubmitter

querystring = {"symbol":"BTC-USD","region":"US"}
request = YahooRequest.YahooRequest("BTC-USD", "US")

response = YahooSubmitter.submit(request)

print(response.text)
