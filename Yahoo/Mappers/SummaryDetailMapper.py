from Yahoo import YahooResponse


def map_summary_detail(summary_text):
    summaryDetail = YahooResponse.SummaryDetail

    previousClose = summary_text["previousClose"]
    summaryDetail.PreviousClose = YahooResponse.PreviousClose(previousClose["raw"], previousClose["fmt"])

    regularMarketOpen = summary_text["regularMarketOpen"]
    summaryDetail.RegularMarketOpen = YahooResponse.RegularMarketOpen(regularMarketOpen["raw"], regularMarketOpen["fmt"])

    twoHundredDayAverage = summary_text["twoHundredDayAverage"]
    summaryDetail.TwoHundredDayAverage = YahooResponse.TwoHundredDayAverage(twoHundredDayAverage["raw"], twoHundredDayAverage["fmt"])

    summaryDetail.TrailingAnnualDividendYield = summary_text["trailingAnnualDividendYield"]
    summaryDetail.PayoutRatio = summary_text["payoutRatio"]

    volume24Hr = summary_text["volume24Hr"]
    summaryDetail.Volume24Hr = YahooResponse.Volume24Hr(volume24Hr["raw"], volume24Hr["fmt"], volume24Hr["longFmt"])

    regularMarketDayHigh = summary_text["regularMarketDayHigh"]
    summaryDetail.RegularMarketDayHigh = YahooResponse.RegularMarketDayHigh(regularMarketDayHigh["raw"], regularMarketDayHigh["fmt"])

    summaryDetail.NavPrice = summary_text["navPrice"]

    averageDailyVolume10Day = summary_text["averageDailyVolume10Day"]
    summaryDetail.AverageDailyVolume10Day = YahooResponse.AverageDailyVolume10Day(averageDailyVolume10Day["raw"], averageDailyVolume10Day["fmt"], averageDailyVolume10Day["longFmt"])

    summaryDetail.TotalAssets = summary_text["totalAssets"]

    regularMarketPreviousClose = summary_text["regularMarketPreviousClose"]
    summaryDetail.RegularMarketPreviousClose = YahooResponse.RegularMarketPreviousClose(regularMarketPreviousClose["raw"], regularMarketPreviousClose["fmt"])

    fiftyDayAverage = summary_text["fiftyDayAverage"]
    summaryDetail.FiftyDayAverage = YahooResponse.FiftyDayAverage(fiftyDayAverage["raw"], fiftyDayAverage["fmt"])

    summaryDetail.TrailingAnnualDividendRate = summary_text["trailingAnnualDividendRate"]

    openElement = summary_text["open"]
    summaryDetail.Open = YahooResponse.Open(openElement["raw"], openElement["fmt"])

    summaryDetail.ToCurrency = summary_text["toCurrency"]

    averageVolume10days = summary_text["averageVolume10days"]
    summaryDetail.AverageVolume10days = YahooResponse.AverageVolume10days(averageVolume10days["raw"], averageVolume10days["fmt"], averageVolume10days["longFmt"])

    summaryDetail.ExpireDate = summary_text["expireDate"]
    summaryDetail.Yield = summary_text["yield"]
    summaryDetail.Algorithm = summary_text["algorithm"]
    summaryDetail.DividendRate = summary_text["dividendRate"]
    summaryDetail.ExDividendDate = summary_text["exDividendDate"]
    summaryDetail.Beta = summary_text["beta"]
    summaryDetail.Currency = summary_text["currency"]
    summaryDetail.LastMarket = summary_text["lastMarket"]
    summaryDetail.MaxSupply = summary_text["maxSupply"]
    summaryDetail.OpenInterest = summary_text["openInterest"]
    summaryDetail.StrikePrice = summary_text["strikePrice"]
    summaryDetail.PriceToSalesTrailing12Months = summary_text["priceToSalesTrailing12Months"]
    summaryDetail.Ask = summary_text["ask"]
    summaryDetail.YtdReturn = summary_text["ytdReturn"]
    summaryDetail.AskSize = summary_text["askSize"]
    summaryDetail.ForwardPE = summary_text["forwardPE"]
    summaryDetail.MaxAge = summary_text["maxAge"]
    summaryDetail.FromCurrency = summary_text["fromCurrency"]
    summaryDetail.FiveYearAvgDividendYield = summary_text["fiveYearAvgDividendYield"]
    summaryDetail.Bid = summary_text["bid"]
    summaryDetail.Tradeable = summary_text["tradeable"]
    summaryDetail.DividendYield = summary_text["dividendYield"]
    summaryDetail.BidSize = summary_text["bidSize"]

    circulatingSupply = summary_text["circulatingSupply"]
    summaryDetail.CirculatingSupply = YahooResponse.CirculatingSupply(circulatingSupply["raw"], circulatingSupply["fmt"], circulatingSupply["longFmt"])

    startDate = summary_text["startDate"]
    summaryDetail.StartDate = YahooResponse.StartDate(startDate["raw"], startDate["fmt"])

    regularMarketDayLow = summary_text["regularMarketDayLow"]
    summaryDetail.RegularMarketDayLow = YahooResponse.RegularMarketDayLow(regularMarketDayLow["raw"], regularMarketDayLow["fmt"])

    priceHint = summary_text["priceHint"]
    summaryDetail.PriceHint = YahooResponse.PriceHint(priceHint["raw"], priceHint["fmt"], priceHint["longFmt"])

    regularMarketVolume = summary_text["regularMarketVolume"]
    summaryDetail.RegularMarketVolume = YahooResponse.RegularMarketVolume(regularMarketVolume["raw"], regularMarketVolume["fmt"], regularMarketVolume["longFmt"])

    marketCap = summary_text["marketCap"]
    summaryDetail.MarketCap = YahooResponse.MarketCap(marketCap["raw"], marketCap["fmt"], marketCap["longFmt"])

    volumeAllCurrencies = summary_text["volumeAllCurrencies"]
    summaryDetail.VolumeAllCurrencies = YahooResponse.VolumeAllCurrencies(volumeAllCurrencies["raw"], volumeAllCurrencies["fmt"], volumeAllCurrencies["longFmt"])

    averageVolume = summary_text["averageVolume"]
    summaryDetail.AverageVolume = YahooResponse.AverageVolume(averageVolume["raw"], averageVolume["fmt"], averageVolume["longFmt"])

    dayLow = summary_text["dayLow"]
    summaryDetail.DayLow = YahooResponse.DayLow(dayLow["raw"], dayLow["fmt"])

    volume = summary_text["volume"]
    summaryDetail.Volume = YahooResponse.Volume(volume["raw"], volume["fmt"], volume["longFmt"])

    fiftyTwoWeekHigh = summary_text["fiftyTwoWeekHigh"]
    summaryDetail.FiftyTwoWeekHigh = YahooResponse.FiftyTwoWeekHigh(fiftyTwoWeekHigh["raw"], fiftyTwoWeekHigh["fmt"])

    fiftyTwoWeekLow = summary_text["fiftyTwoWeekLow"]
    summaryDetail.FiftyTwoWeekLow = YahooResponse.FiftyTwoWeekLow(fiftyTwoWeekLow["raw"], fiftyTwoWeekLow["fmt"])

    dayHigh = summary_text["dayHigh"]
    summaryDetail.DayHigh = YahooResponse.DayHigh(dayHigh["raw"], dayHigh["fmt"])

    return summaryDetail
