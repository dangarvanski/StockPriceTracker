from Yahoo import YahooResponse


def map_price(price_text):
    price = YahooResponse.Price

    price.QuoteSourceName = price_text["quoteSourceName"]

    regularMarketOpen = price_text["regularMarketOpen"]
    price.RegularMarketOpen = YahooResponse.RegularMarketOpen(regularMarketOpen["raw"], regularMarketOpen["fmt"])

    averageDailyVolume3Month = price_text["averageDailyVolume3Month"]
    price.AverageDailyVolume3Month = YahooResponse.AverageDailyVolume3Month(averageDailyVolume3Month["raw"], averageDailyVolume3Month["fmt"], averageDailyVolume3Month["longFmt"])

    price.Exchange = price_text["exchange"]
    price.RegularMarketTime = price_text["regularMarketTime"]

    volume24Hr = price_text["volume24Hr"]
    price.Volume24Hr = YahooResponse.Volume24Hr(volume24Hr["raw"], volume24Hr["fmt"], volume24Hr["longFmt"])

    regularMarketDayHigh = price_text["regularMarketDayHigh"]
    price.RegularMarketDayHigh = YahooResponse.RegularMarketDayHigh(regularMarketDayHigh["raw"], regularMarketDayHigh["fmt"])

    price.ShortName = price_text["shortName"]
    price.LongName = price_text["longName"]

    averageDailyVolume10Day = price_text["averageDailyVolume10Day"]
    price.AverageDailyVolume10Day = YahooResponse.AverageDailyVolume10Day(averageDailyVolume10Day["raw"], averageDailyVolume10Day["fmt"], averageDailyVolume10Day["longFmt"])

    regularMarketChange = price_text["regularMarketChange"]
    price.RegularMarketChange = YahooResponse.RegularMarketChange(regularMarketChange["raw"], regularMarketChange["fmt"])

    price.CurrencySymbol = price_text["currencySymbol"]

    regularMarketPreviousClose = price_text["regularMarketPreviousClose"]
    price.RegularMarketPreviousClose = YahooResponse.RegularMarketPreviousClose(regularMarketPreviousClose["raw"], regularMarketPreviousClose["fmt"])

    price.PreMarketPrice = price_text["preMarketPrice"]
    price.ExchangeDataDelayedBy = price_text["exchangeDataDelayedBy"]
    price.ToCurrency = price_text["toCurrency"]
    price.PostMarketChange = price_text["postMarketChange"]
    price.PostMarketPrice = price_text["postMarketPrice"]
    price.ExchangeName = price_text["exchangeName"]
    price.PreMarketChange = price_text["preMarketChange"]

    circulatingSupply = price_text["circulatingSupply"]
    price.CirculatingSupply = YahooResponse.CirculatingSupply(circulatingSupply["raw"], circulatingSupply["fmt"], circulatingSupply["longFmt"])

    regularMarketDayLow = price_text["regularMarketDayLow"]
    price.RegularMarketDayLow = YahooResponse.RegularMarketDayLow(regularMarketDayLow["raw"], regularMarketDayLow["fmt"])

    priceHint = price_text["priceHint"]
    price.PriceHint = YahooResponse.PriceHint(priceHint["raw"], priceHint["fmt"], priceHint["longFmt"])

    price.Currency = price_text["currency"]

    regularMarketPrice = price_text["regularMarketPrice"]
    price.RegularMarketPrice = YahooResponse.RegularMarketPrice(regularMarketPrice["raw"], regularMarketPrice["fmt"])

    regularMarketVolume = price_text["regularMarketVolume"]
    price.RegularMarketVolume = YahooResponse.RegularMarketVolume(regularMarketVolume["raw"], regularMarketVolume["fmt"], regularMarketVolume["longFmt"])

    price.LastMarket = price_text["lastMarket"]
    price.RegularMarketSource = price_text["regularMarketSource"]
    price.OpenInterest = price_text["openInterest"]
    price.MarketState = price_text["marketState"]
    price.UnderlyingSymbol = price_text["underlyingSymbol"]

    marketCap = price_text["marketCap"]
    price.MarketCap = YahooResponse.MarketCap(marketCap["raw"], marketCap["fmt"], marketCap["longFmt"])

    price.QuoteType = price_text["quoteType"]

    volumeAllCurrencies = price_text["volumeAllCurrencies"]
    price.VolumeAllCurrencies = YahooResponse.VolumeAllCurrencies(volumeAllCurrencies["raw"], volumeAllCurrencies["fmt"], volumeAllCurrencies["longFmt"])

    price.StrikePrice = price_text["strikePrice"]
    price.Symbol = price_text["symbol"]
    price.MaxAge = price_text["maxAge"]
    price.FromCurrency = price_text["fromCurrency"]

    regularMarketChangePercent = price_text["regularMarketChangePercent"]
    price.RegularMarketChangePercent = YahooResponse.RegularMarketChangePercent(regularMarketChangePercent["raw"], regularMarketChangePercent["fmt"])

    return price
