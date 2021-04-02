from Yahoo import YahooRequest
from Yahoo import YahooSubmitter
from Yahoo.Mappers import ResponseMapper
import json

request = YahooRequest.YahooRequest("BTC-USD", "US")
#request = YahooRequest.YahooRequest("TSLA", "US")

response = YahooSubmitter.submit(request)

#Coverting response to json
responseJson = json.loads(response.text)

responsePython = ResponseMapper.map_response(responseJson)

print('Assets Company Officers: ' + str(responsePython.AssetProfile.CompanyOfficers))
print('Assets Name: ' + str(responsePython.AssetProfile.Name))