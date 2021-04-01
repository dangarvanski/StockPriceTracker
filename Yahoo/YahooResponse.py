class YahooResponse:
    FinancialsTemplate = None
    Price = None

    # getter method
    def get_financials_template(self):
        return self.financialsTemplate

    # setter method
    def set_financials_template(self, x):
        self.financialsTemplate = x
    # getter method

    def get_price(self):
        return self.Price

    # setter method
    def set_price(self, x):
        self.Price = x


class RegularMarketOpen:
    def __init__(self, raw, fmt):
        self.raw = raw
        self.fmt = fmt


class AverageDailyVolume3Month:
    def __init__(self, raw, fmt, long_fmt):
        self.raw = raw
        self.fmt = fmt
        self.longFmt = long_fmt


class Price:
    QuoteSourceName = None
    RegularMarketOpen = RegularMarketOpen(None, None)
    AverageDailyVolume3Month = AverageDailyVolume3Month(None, None, None)
    Exchange = None
    RegularMarketTime = None
    Volume24Hr = None
    RegularMarketDayHigh = None
    ShortName = None
    AverageDailyVolume10Day = None
    LongName = None
    RegularMarketChange = None
    CurrencySymbol = None
    RegularMarketPreviousClose = None
    PreMarketPrice = None
    ExchangeDataDelayedBy = 0
    ToCurrency = None
    PostMarketChange = None
    PostMarketPrice = None
    ExchangeName = None
    PreMarketChange = None
    CirculatingSupply = None
    RegularMarketDayLow = None
    PriceHint = None
    Currency = None
    RegularMarketPrice = None
    RegularMarketVolume = None
    LastMarket = None
    RegularMarketSource = None
    OpenInterest = None
    MarketState = None
    UnderlyingSymbol = None
    MarketCap = None
    QuoteType = None
    VolumeAllCurrencies = None
    StrikePrice = None
    Symbol = None
    MaxAge = 0
    FromCurrency = None
    RegularMarketChangePercent = None


class Volume24Hr:
    raw = 0
    fmt = 0
    longFmt = 0


class RegularMarketDayHigh:
    raw = 0
    fmt = 0


class AverageDailyVolume10Day:
    raw = 0
    fmt = 0
    longFmt = 0


class RegularMarketChange:
    raw = 0
    fmt = 0


class RegularMarketPreviousClose:
    raw = 0
    fmt = 0


class CirculatingSupply:
    raw = 0
    fmt = 0
    longFmt = 0


class RegularMarketDayLow:
    raw = 0
    fmt = 0


class PriceHint:
    raw = 0
    fmt = 0
    longFmt = 0


class RegularMarketPrice:
    raw = 0
    fmt = 0


class RegularMarketVolume:
    raw = 0
    fmt = 0
    longFmt = 0


class MarketCap:
    raw = 0
    fmt = 0
    longFmt = 0


class VolumeAllCurrencies:
    raw = 0
    fmt = 0
    longFmt = 0


class RegularMarketChangePercent:
    raw = 0
    fmt = 0
