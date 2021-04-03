from Yahoo import YahooResponse
from Yahoo import YahooResponseV2
from Yahoo.Mappers import PriceMapper
from Yahoo.Mappers import QuoteTypeMapper
from Yahoo.Mappers import SummaryDetailMapper
from Yahoo.Mappers import AssetProfileMapper


def map_response(json_response):
    response = YahooResponse.YahooResponse

    mappedPrice = PriceMapper.map_price(json_response["price"])
    mappedQuoteType = QuoteTypeMapper.map_quote_type(json_response["quoteType"])
    mappedSummaryDetail = SummaryDetailMapper.map_summary_detail(json_response["summaryDetail"])
    mappedAssetProfile = AssetProfileMapper.map_asset_profile(json_response["assetProfile"])

    response.FinancialsTemplate = json_response["financialsTemplate"]
    response.Price = mappedPrice
    response.SecFilings = json_response["secFilings"]
    response.QuoteType = mappedQuoteType
    response.CalendarEvents = json_response["calendarEvents"]
    response.SummaryDetail = mappedSummaryDetail
    response.Symbol = json_response["symbol"]
    response.AssetProfile = mappedAssetProfile
    response.PageViews = json_response["pageViews"]

    return response


def map_responseV2(json_response):
    response = YahooResponseV2

    financeTemplate = json_response["financialsTemplate"]

    if len(financeTemplate) != 0:
        response.FinancialsTemplate.code = financeTemplate["code"]
        response.FinancialsTemplate.max_age = financeTemplate["maxAge"]
    else:
        response.FinancialsTemplate.code = "Empty bruh"
        response.FinancialsTemplate.max_age = "It's empty"
    return response
