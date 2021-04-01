from Yahoo import Request
from Yahoo import YahooSubmitter

querystring = {"symbol":"BTC-USD","region":"US"}
request = Request.Request("BTC-USD", "US")

response = YahooSubmitter.submit(request)

print(response.text)
