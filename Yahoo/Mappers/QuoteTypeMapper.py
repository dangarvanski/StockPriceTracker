from Yahoo import YahooResponse


def map_quote_type(quote_type_text):
    quoteType = YahooResponse.QuoteType

    quoteType.Exchange = quote_type_text["exchange"]
    quoteType.ShortName = quote_type_text["shortName"]
    quoteType.ExchangeTimezoneName = quote_type_text["exchangeTimezoneName"]
    quoteType.ExchangeTimezoneShortName = quote_type_text["exchangeTimezoneShortName"]
    quoteType.IsEsgPopulated = quote_type_text["isEsgPopulated"]
    quoteType.GmtOffSetMilliseconds = quote_type_text["gmtOffSetMilliseconds"]
    quoteType.QuoteType = quote_type_text["quoteType"]
    quoteType.Symbol = quote_type_text["symbol"]
    quoteType.MessageBoardId = quote_type_text["messageBoardId"]
    quoteType.Market = quote_type_text["market"]