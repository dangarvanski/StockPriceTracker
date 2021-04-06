from Yahoo import YahooResponse
from Yahoo.Mappers import PriceMapper
from Yahoo.Mappers import QuoteTypeMapper


def map_response(json_reponse):
    response = YahooResponse.YahooResponse

    mappedPrice = PriceMapper.map_price(json_reponse["price"])
    mappedQuoteType = QuoteTypeMapper.map_quote_type(json_reponse["quoteType"])

    response.FinancialsTemplate = json_reponse["financialsTemplate"]
    response.Price = mappedPrice
    response.SecFilings = json_reponse["secFilings"]
    response.QuoteType = mappedQuoteType
    response.CalendarEvents = json_reponse["calendarEvents"]

    return response
