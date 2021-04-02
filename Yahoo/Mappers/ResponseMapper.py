from Yahoo import YahooResponse
from Yahoo.Mappers import PriceMapper
from Yahoo.Mappers import QuoteTypeMapper
from Yahoo.Mappers import SummaryDetailMapper
from Yahoo.Mappers import AssetProfileMapper


def map_response(json_reponse):
    response = YahooResponse.YahooResponse

    mappedPrice = PriceMapper.map_price(json_reponse["price"])
    mappedQuoteType = QuoteTypeMapper.map_quote_type(json_reponse["quoteType"])
    mappedSummaryDetail = SummaryDetailMapper.map_summary_detail(json_reponse["summaryDetail"])
    mappedAssetProfile = AssetProfileMapper.map_asset_profile(json_reponse["assetProfile"])

    response.FinancialsTemplate = json_reponse["financialsTemplate"]
    response.Price = mappedPrice
    response.SecFilings = json_reponse["secFilings"]
    response.QuoteType = mappedQuoteType
    response.CalendarEvents = json_reponse["calendarEvents"]
    response.SummaryDetail = mappedSummaryDetail
    response.Symbol = json_reponse["symbol"]
    response.AssetProfile = mappedAssetProfile
    response.PageViews = json_reponse["pageViews"]

    return response
