class YahooResponse:
    FinancialsTemplate = None
    Price = None
    SecFilings = None
    QuoteType = None
    CalendarEvents = None
    SummaryDetail = None
    Symbol = None
    AssetProfile = None
    PageViews = None


class RegularMarketOpen:
    def __init__(self, raw, fmt):
        self.raw = raw
        self.fmt = fmt


class AverageDailyVolume3Month:
    def __init__(self, raw, fmt, long_fmt):
        self.raw = raw
        self.fmt = fmt
        self.longFmt = long_fmt


class Volume24Hr:
    def __init__(self, raw, fmt, long_fmt):
        self.raw = raw
        self.fmt = fmt
        self.longFmt = long_fmt


class RegularMarketDayHigh:
    def __init__(self, raw, fmt):
        self.raw = raw
        self.fmt = fmt


class AverageDailyVolume10Day:
    def __init__(self, raw, fmt, long_fmt):
        self.raw = raw
        self.fmt = fmt
        self.longFmt = long_fmt


class RegularMarketChange:
    def __init__(self, raw, fmt):
        self.raw = raw
        self.fmt = fmt


class RegularMarketPreviousClose:
    def __init__(self, raw, fmt):
        self.raw = raw
        self.fmt = fmt


class CirculatingSupply:
    def __init__(self, raw, fmt, long_fmt):
        self.raw = raw
        self.fmt = fmt
        self.longFmt = long_fmt


class RegularMarketDayLow:
    def __init__(self, raw, fmt):
        self.raw = raw
        self.fmt = fmt


class PriceHint:
    def __init__(self, raw, fmt, long_fmt):
        self.raw = raw
        self.fmt = fmt
        self.longFmt = long_fmt


class RegularMarketPrice:
    def __init__(self, raw, fmt):
        self.raw = raw
        self.fmt = fmt


class RegularMarketVolume:
    def __init__(self, raw, fmt, long_fmt):
        self.raw = raw
        self.fmt = fmt
        self.longFmt = long_fmt


class MarketCap:
    def __init__(self, raw, fmt, long_fmt):
        self.raw = raw
        self.fmt = fmt
        self.longFmt = long_fmt


class VolumeAllCurrencies:
    def __init__(self, raw, fmt, long_fmt):
        self.raw = raw
        self.fmt = fmt
        self.longFmt = long_fmt


class RegularMarketChangePercent:
    def __init__(self, raw, fmt):
        self.raw = raw
        self.fmt = fmt


class Price:
    QuoteSourceName = None
    RegularMarketOpen = RegularMarketOpen(None, None)
    AverageDailyVolume3Month = AverageDailyVolume3Month(None, None, None)
    Exchange = None
    RegularMarketTime = None
    Volume24Hr = Volume24Hr(None, None, None)
    RegularMarketDayHigh = RegularMarketDayHigh(None, None)
    ShortName = None
    AverageDailyVolume10Day = AverageDailyVolume10Day(None, None, None)
    LongName = None
    RegularMarketChange = RegularMarketChange(None, None)
    CurrencySymbol = None
    RegularMarketPreviousClose = RegularMarketPreviousClose(None, None)
    PreMarketPrice = None
    ExchangeDataDelayedBy = 0
    ToCurrency = None
    PostMarketChange = None
    PostMarketPrice = None
    ExchangeName = None
    PreMarketChange = None
    CirculatingSupply = CirculatingSupply(None, None, None)
    RegularMarketDayLow = RegularMarketDayLow(None, None)
    PriceHint = PriceHint(None, None, None)
    Currency = None
    RegularMarketPrice = RegularMarketPrice(None, None)
    RegularMarketVolume = RegularMarketVolume(None, None, None)
    LastMarket = None
    RegularMarketSource = None
    OpenInterest = None
    MarketState = None
    UnderlyingSymbol = None
    MarketCap = MarketCap(None, None, None)
    QuoteType = None
    VolumeAllCurrencies = VolumeAllCurrencies(None, None, None)
    StrikePrice = None
    Symbol = None
    MaxAge = 0
    FromCurrency = None
    RegularMarketChangePercent = RegularMarketChangePercent(None, None)


class QuoteType:
    Exchange = None
    ShortName = None
    ExchangeTimezoneName = None
    ExchangeTimezoneShortName = None
    IsEsgPopulated = None
    GmtOffSetMilliseconds = None
    QuoteType = None
    Symbol = None
    MessageBoardId = None
    Market = None


class PreviousClose:
    def __init__(self, raw, fmt):
        self.raw = raw
        self.fmt = fmt


class TwoHundredDayAverage:
    def __init__(self, raw, fmt):
        self.raw = raw
        self.fmt = fmt


class FiftyDayAverage:
    def __init__(self, raw, fmt):
        self.raw = raw
        self.fmt = fmt


class Open:
    def __init__(self, raw, fmt):
        self.raw = raw
        self.fmt = fmt


class AverageVolume10days:
    def __init__(self, raw, fmt, long_fmt):
        self.raw = raw
        self.fmt = fmt
        self.longFmt = long_fmt


class StartDate:
    def __init__(self, raw, fmt):
        self.raw = raw
        self.fmt = fmt


class AverageVolume:
    def __init__(self, raw, fmt, long_fmt):
        self.raw = raw
        self.fmt = fmt
        self.longFmt = long_fmt


class DayLow:
    def __init__(self, raw, fmt):
        self.raw = raw
        self.fmt = fmt


class Volume:
    def __init__(self, raw, fmt, long_fmt):
        self.raw = raw
        self.fmt = fmt
        self.longFmt = long_fmt


class FiftyTwoWeekHigh:
    def __init__(self, raw, fmt):
        self.raw = raw
        self.fmt = fmt


class FiftyTwoWeekLow:
    def __init__(self, raw, fmt):
        self.raw = raw
        self.fmt = fmt


class DayHigh:
    def __init__(self, raw, fmt):
        self.raw = raw
        self.fmt = fmt


class SummaryDetail:
    PreviousClose = PreviousClose(None, None)
    RegularMarketOpen = RegularMarketOpen(None, None)
    TwoHundredDayAverage = TwoHundredDayAverage(None, None)
    TrailingAnnualDividendYield = None
    PayoutRatio = None
    Volume24Hr = Volume24Hr(None, None, None)
    RegularMarketDayHigh = RegularMarketDayHigh(None, None)
    NavPrice = None
    AverageDailyVolume10Day = AverageDailyVolume10Day(None, None, None)
    TotalAssets = None
    RegularMarketPreviousClose = RegularMarketPreviousClose(None, None)
    FiftyDayAverage = FiftyDayAverage(None, None)
    TrailingAnnualDividendRate = None
    Open = Open(None, None)
    ToCurrency = None
    AverageVolume10days = AverageVolume10days(None, None, None)
    ExpireDate = None
    Yield = None
    Algorithm = None
    DividendRate = None
    ExDividendDate = None
    Beta = None
    CirculatingSupply = CirculatingSupply(None, None, None)
    StartDate = StartDate(None, None)
    RegularMarketDayLow = RegularMarketDayLow(None, None)
    PriceHint = PriceHint(None, None, None)
    Currency = None
    RegularMarketVolume = RegularMarketVolume(None, None, None)
    LastMarket = None
    MaxSupply = None
    OpenInterest = None
    MarketCap = MarketCap(None, None, None)
    VolumeAllCurrencies = VolumeAllCurrencies(None, None, None)
    StrikePrice = None
    AverageVolume = AverageVolume(None, None, None)
    PriceToSalesTrailing12Months = None
    DayLow = DayLow(None, None)
    Ask = None
    YtdReturn = None
    AskSize = None
    Volume = Volume(None, None, None)
    FiftyTwoWeekHigh = FiftyTwoWeekHigh(None, None)
    ForwardPE = None
    MaxAge = None
    FromCurrency = None
    FiveYearAvgDividendYield = None
    FiftyTwoWeekLow = FiftyTwoWeekLow(None, None)
    Bid = None
    Tradeable = None
    DividendYield = None
    BidSize = None
    DayHigh = DayHigh(None, None)


class AssetProfile:
    CompanyOfficers = None
    Name = None
    StartDate = None
    Description = None
    MaxAge = None
