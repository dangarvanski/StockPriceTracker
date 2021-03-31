import APICall
import Stock
import ApiValues
import json

def get_stockPrice(htmlText):
    scriptElements = htmlText.find_all('div', {'class': 'D(ib) Va(m) Maw(65%) Ov(h)'})
    if len(scriptElements) == 0:
        return 'Stock price not found!'
    else:
        stockPrice = scriptElements[0].find('span')
        return stockPrice.text

def get_stockName(htmlText):
    scriptElements = htmlText.find_all('div', {
        'class': 'D(ib) Mt(-5px) Mend(20px) Maw(56%)--tab768 Maw(52%) Ov(h) smartphone_Maw(85%) smartphone_Mend(0px)'})
    if len(scriptElements) == 0:
        return 'Stock name not found!'
    else:
        stockName = scriptElements[0].find('h1')
        return stockName.text

def get_StockWebPageData(apiLink):
    soup = APICall.YahooAPICall.get_websiteData(apiLink)
    price = get_stockPrice(soup)
    name = get_stockName(soup)
    return Stock.Stock(name, price)

def get_Info(response, dataType):
    responseJson = json.loads(response)
    quote = responseJson["quoteResponse"]
    result = quote["result"]
    for item in result[0].items():
        if (item[0] == dataType):
            return(item[1])

def get_StockUpdate(apiLink):
    response = APICall.YahooAPICall.get_updateData(apiLink)
    return response
