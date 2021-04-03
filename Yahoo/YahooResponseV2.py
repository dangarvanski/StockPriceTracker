# This code parses date/times, so please
#
#     pip install python-dateutil
#
# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = welcome_from_dict(json.loads(json_string))

from typing import Optional, Any, List, TypeVar, Type, cast, Callable
from enum import Enum
from datetime import datetime
import dateutil.parser


T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def to_float(x: Any) -> float:
    assert isinstance(x, float)
    return x


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


class AverageDailyVolume10Day:
    raw: int
    fmt: Optional[str]
    long_fmt: str

    def __init__(self, raw: int, fmt: Optional[str], long_fmt: str) -> None:
        self.raw = raw
        self.fmt = fmt
        self.long_fmt = long_fmt

    @staticmethod
    def from_dict(obj: Any) -> 'AverageDailyVolume10Day':
        assert isinstance(obj, dict)
        raw = from_int(obj.get("raw"))
        fmt = from_union([from_none, from_str], obj.get("fmt"))
        long_fmt = from_str(obj.get("longFmt"))
        return AverageDailyVolume10Day(raw, fmt, long_fmt)

    def to_dict(self) -> dict:
        result: dict = {}
        result["raw"] = from_int(self.raw)
        result["fmt"] = from_union([from_none, from_str], self.fmt)
        result["longFmt"] = from_str(self.long_fmt)
        return result


class CompanyOfficer:
    total_pay: Optional[AverageDailyVolume10Day]
    exercised_value: AverageDailyVolume10Day
    year_born: Optional[int]
    name: str
    title: str
    max_age: int
    fiscal_year: Optional[int]
    unexercised_value: AverageDailyVolume10Day
    age: Optional[int]

    def __init__(self, total_pay: Optional[AverageDailyVolume10Day], exercised_value: AverageDailyVolume10Day, year_born: Optional[int], name: str, title: str, max_age: int, fiscal_year: Optional[int], unexercised_value: AverageDailyVolume10Day, age: Optional[int]) -> None:
        self.total_pay = total_pay
        self.exercised_value = exercised_value
        self.year_born = year_born
        self.name = name
        self.title = title
        self.max_age = max_age
        self.fiscal_year = fiscal_year
        self.unexercised_value = unexercised_value
        self.age = age

    @staticmethod
    def from_dict(obj: Any) -> 'CompanyOfficer':
        assert isinstance(obj, dict)
        total_pay = from_union([AverageDailyVolume10Day.from_dict, from_none], obj.get("totalPay"))
        exercised_value = AverageDailyVolume10Day.from_dict(obj.get("exercisedValue"))
        year_born = from_union([from_int, from_none], obj.get("yearBorn"))
        name = from_str(obj.get("name"))
        title = from_str(obj.get("title"))
        max_age = from_int(obj.get("maxAge"))
        fiscal_year = from_union([from_int, from_none], obj.get("fiscalYear"))
        unexercised_value = AverageDailyVolume10Day.from_dict(obj.get("unexercisedValue"))
        age = from_union([from_int, from_none], obj.get("age"))
        return CompanyOfficer(total_pay, exercised_value, year_born, name, title, max_age, fiscal_year, unexercised_value, age)

    def to_dict(self) -> dict:
        result: dict = {}
        result["totalPay"] = from_union([lambda x: to_class(AverageDailyVolume10Day, x), from_none], self.total_pay)
        result["exercisedValue"] = to_class(AverageDailyVolume10Day, self.exercised_value)
        result["yearBorn"] = from_union([from_int, from_none], self.year_born)
        result["name"] = from_str(self.name)
        result["title"] = from_str(self.title)
        result["maxAge"] = from_int(self.max_age)
        result["fiscalYear"] = from_union([from_int, from_none], self.fiscal_year)
        result["unexercisedValue"] = to_class(AverageDailyVolume10Day, self.unexercised_value)
        result["age"] = from_union([from_int, from_none], self.age)
        return result


class AssetProfile:
    zip: int
    sector: str
    full_time_employees: int
    compensation_risk: int
    audit_risk: int
    long_business_summary: str
    city: str
    phone: str
    state: str
    share_holder_rights_risk: int
    compensation_as_of_epoch_date: int
    governance_epoch_date: int
    board_risk: int
    country: str
    company_officers: List[CompanyOfficer]
    website: str
    max_age: int
    overall_risk: int
    address1: str
    industry: str

    def __init__(self, zip: int, sector: str, full_time_employees: int, compensation_risk: int, audit_risk: int, long_business_summary: str, city: str, phone: str, state: str, share_holder_rights_risk: int, compensation_as_of_epoch_date: int, governance_epoch_date: int, board_risk: int, country: str, company_officers: List[CompanyOfficer], website: str, max_age: int, overall_risk: int, address1: str, industry: str) -> None:
        self.zip = zip
        self.sector = sector
        self.full_time_employees = full_time_employees
        self.compensation_risk = compensation_risk
        self.audit_risk = audit_risk
        self.long_business_summary = long_business_summary
        self.city = city
        self.phone = phone
        self.state = state
        self.share_holder_rights_risk = share_holder_rights_risk
        self.compensation_as_of_epoch_date = compensation_as_of_epoch_date
        self.governance_epoch_date = governance_epoch_date
        self.board_risk = board_risk
        self.country = country
        self.company_officers = company_officers
        self.website = website
        self.max_age = max_age
        self.overall_risk = overall_risk
        self.address1 = address1
        self.industry = industry

    @staticmethod
    def from_dict(obj: Any) -> 'AssetProfile':
        assert isinstance(obj, dict)
        zip = int(from_str(obj.get("zip")))
        sector = from_str(obj.get("sector"))
        full_time_employees = from_int(obj.get("fullTimeEmployees"))
        compensation_risk = from_int(obj.get("compensationRisk"))
        audit_risk = from_int(obj.get("auditRisk"))
        long_business_summary = from_str(obj.get("longBusinessSummary"))
        city = from_str(obj.get("city"))
        phone = from_str(obj.get("phone"))
        state = from_str(obj.get("state"))
        share_holder_rights_risk = from_int(obj.get("shareHolderRightsRisk"))
        compensation_as_of_epoch_date = from_int(obj.get("compensationAsOfEpochDate"))
        governance_epoch_date = from_int(obj.get("governanceEpochDate"))
        board_risk = from_int(obj.get("boardRisk"))
        country = from_str(obj.get("country"))
        company_officers = from_list(CompanyOfficer.from_dict, obj.get("companyOfficers"))
        website = from_str(obj.get("website"))
        max_age = from_int(obj.get("maxAge"))
        overall_risk = from_int(obj.get("overallRisk"))
        address1 = from_str(obj.get("address1"))
        industry = from_str(obj.get("industry"))
        return AssetProfile(zip, sector, full_time_employees, compensation_risk, audit_risk, long_business_summary, city, phone, state, share_holder_rights_risk, compensation_as_of_epoch_date, governance_epoch_date, board_risk, country, company_officers, website, max_age, overall_risk, address1, industry)

    def to_dict(self) -> dict:
        result: dict = {}
        result["zip"] = from_str(str(self.zip))
        result["sector"] = from_str(self.sector)
        result["fullTimeEmployees"] = from_int(self.full_time_employees)
        result["compensationRisk"] = from_int(self.compensation_risk)
        result["auditRisk"] = from_int(self.audit_risk)
        result["longBusinessSummary"] = from_str(self.long_business_summary)
        result["city"] = from_str(self.city)
        result["phone"] = from_str(self.phone)
        result["state"] = from_str(self.state)
        result["shareHolderRightsRisk"] = from_int(self.share_holder_rights_risk)
        result["compensationAsOfEpochDate"] = from_int(self.compensation_as_of_epoch_date)
        result["governanceEpochDate"] = from_int(self.governance_epoch_date)
        result["boardRisk"] = from_int(self.board_risk)
        result["country"] = from_str(self.country)
        result["companyOfficers"] = from_list(lambda x: to_class(CompanyOfficer, x), self.company_officers)
        result["website"] = from_str(self.website)
        result["maxAge"] = from_int(self.max_age)
        result["overallRisk"] = from_int(self.overall_risk)
        result["address1"] = from_str(self.address1)
        result["industry"] = from_str(self.industry)
        return result


class DividendDate:
    pass

    def __init__(self, ) -> None:
        pass

    @staticmethod
    def from_dict(obj: Any) -> 'DividendDate':
        assert isinstance(obj, dict)
        return DividendDate()

    def to_dict(self) -> dict:
        result: dict = {}
        return result


class PostMarketChange:
    raw: float
    fmt: str

    def __init__(self, raw: float, fmt: str) -> None:
        self.raw = raw
        self.fmt = fmt

    @staticmethod
    def from_dict(obj: Any) -> 'PostMarketChange':
        assert isinstance(obj, dict)
        raw = from_float(obj.get("raw"))
        fmt = from_str(obj.get("fmt"))
        return PostMarketChange(raw, fmt)

    def to_dict(self) -> dict:
        result: dict = {}
        result["raw"] = to_float(self.raw)
        result["fmt"] = from_str(self.fmt)
        return result


class Earnings:
    earnings_date: List[PostMarketChange]
    earnings_average: PostMarketChange
    earnings_low: PostMarketChange
    earnings_high: PostMarketChange
    revenue_average: AverageDailyVolume10Day
    revenue_low: AverageDailyVolume10Day
    revenue_high: AverageDailyVolume10Day

    def __init__(self, earnings_date: List[PostMarketChange], earnings_average: PostMarketChange, earnings_low: PostMarketChange, earnings_high: PostMarketChange, revenue_average: AverageDailyVolume10Day, revenue_low: AverageDailyVolume10Day, revenue_high: AverageDailyVolume10Day) -> None:
        self.earnings_date = earnings_date
        self.earnings_average = earnings_average
        self.earnings_low = earnings_low
        self.earnings_high = earnings_high
        self.revenue_average = revenue_average
        self.revenue_low = revenue_low
        self.revenue_high = revenue_high

    @staticmethod
    def from_dict(obj: Any) -> 'Earnings':
        assert isinstance(obj, dict)
        earnings_date = from_list(PostMarketChange.from_dict, obj.get("earningsDate"))
        earnings_average = PostMarketChange.from_dict(obj.get("earningsAverage"))
        earnings_low = PostMarketChange.from_dict(obj.get("earningsLow"))
        earnings_high = PostMarketChange.from_dict(obj.get("earningsHigh"))
        revenue_average = AverageDailyVolume10Day.from_dict(obj.get("revenueAverage"))
        revenue_low = AverageDailyVolume10Day.from_dict(obj.get("revenueLow"))
        revenue_high = AverageDailyVolume10Day.from_dict(obj.get("revenueHigh"))
        return Earnings(earnings_date, earnings_average, earnings_low, earnings_high, revenue_average, revenue_low, revenue_high)

    def to_dict(self) -> dict:
        result: dict = {}
        result["earningsDate"] = from_list(lambda x: to_class(PostMarketChange, x), self.earnings_date)
        result["earningsAverage"] = to_class(PostMarketChange, self.earnings_average)
        result["earningsLow"] = to_class(PostMarketChange, self.earnings_low)
        result["earningsHigh"] = to_class(PostMarketChange, self.earnings_high)
        result["revenueAverage"] = to_class(AverageDailyVolume10Day, self.revenue_average)
        result["revenueLow"] = to_class(AverageDailyVolume10Day, self.revenue_low)
        result["revenueHigh"] = to_class(AverageDailyVolume10Day, self.revenue_high)
        return result


class CalendarEvents:
    max_age: int
    earnings: Earnings
    ex_dividend_date: DividendDate
    dividend_date: DividendDate

    def __init__(self, max_age: int, earnings: Earnings, ex_dividend_date: DividendDate, dividend_date: DividendDate) -> None:
        self.max_age = max_age
        self.earnings = earnings
        self.ex_dividend_date = ex_dividend_date
        self.dividend_date = dividend_date

    @staticmethod
    def from_dict(obj: Any) -> 'CalendarEvents':
        assert isinstance(obj, dict)
        max_age = from_int(obj.get("maxAge"))
        earnings = Earnings.from_dict(obj.get("earnings"))
        ex_dividend_date = DividendDate.from_dict(obj.get("exDividendDate"))
        dividend_date = DividendDate.from_dict(obj.get("dividendDate"))
        return CalendarEvents(max_age, earnings, ex_dividend_date, dividend_date)

    def to_dict(self) -> dict:
        result: dict = {}
        result["maxAge"] = from_int(self.max_age)
        result["earnings"] = to_class(Earnings, self.earnings)
        result["exDividendDate"] = to_class(DividendDate, self.ex_dividend_date)
        result["dividendDate"] = to_class(DividendDate, self.dividend_date)
        return result


class FinancialsTemplate:
    code: str
    max_age: int

    def __init__(self, code: str, max_age: int) -> None:
        self.code = code
        self.max_age = max_age

    @staticmethod
    def from_dict(obj: Any) -> 'FinancialsTemplate':
        assert isinstance(obj, dict)
        code = from_str(obj.get("code"))
        max_age = from_int(obj.get("maxAge"))
        return FinancialsTemplate(code, max_age)

    def to_dict(self) -> dict:
        result: dict = {}
        result["code"] = from_str(self.code)
        result["maxAge"] = from_int(self.max_age)
        return result


class PageViews:
    short_term_trend: str
    mid_term_trend: str
    long_term_trend: str
    max_age: int

    def __init__(self, short_term_trend: str, mid_term_trend: str, long_term_trend: str, max_age: int) -> None:
        self.short_term_trend = short_term_trend
        self.mid_term_trend = mid_term_trend
        self.long_term_trend = long_term_trend
        self.max_age = max_age

    @staticmethod
    def from_dict(obj: Any) -> 'PageViews':
        assert isinstance(obj, dict)
        short_term_trend = from_str(obj.get("shortTermTrend"))
        mid_term_trend = from_str(obj.get("midTermTrend"))
        long_term_trend = from_str(obj.get("longTermTrend"))
        max_age = from_int(obj.get("maxAge"))
        return PageViews(short_term_trend, mid_term_trend, long_term_trend, max_age)

    def to_dict(self) -> dict:
        result: dict = {}
        result["shortTermTrend"] = from_str(self.short_term_trend)
        result["midTermTrend"] = from_str(self.mid_term_trend)
        result["longTermTrend"] = from_str(self.long_term_trend)
        result["maxAge"] = from_int(self.max_age)
        return result


class Price:
    quote_source_name: str
    regular_market_open: PostMarketChange
    average_daily_volume3_month: AverageDailyVolume10Day
    exchange: str
    regular_market_time: int
    volume24_hr: DividendDate
    regular_market_day_high: PostMarketChange
    short_name: str
    average_daily_volume10_day: AverageDailyVolume10Day
    long_name: str
    regular_market_change: PostMarketChange
    currency_symbol: str
    regular_market_previous_close: PostMarketChange
    post_market_time: int
    pre_market_price: DividendDate
    exchange_data_delayed_by: int
    to_currency: None
    post_market_change: PostMarketChange
    post_market_price: PostMarketChange
    exchange_name: str
    pre_market_change: DividendDate
    circulating_supply: DividendDate
    regular_market_day_low: PostMarketChange
    price_hint: AverageDailyVolume10Day
    currency: str
    regular_market_price: PostMarketChange
    regular_market_volume: AverageDailyVolume10Day
    last_market: None
    regular_market_source: str
    open_interest: DividendDate
    market_state: str
    underlying_symbol: None
    market_cap: AverageDailyVolume10Day
    quote_type: str
    volume_all_currencies: DividendDate
    post_market_source: str
    strike_price: DividendDate
    symbol: str
    post_market_change_percent: PostMarketChange
    pre_market_source: str
    max_age: int
    from_currency: None
    regular_market_change_percent: PostMarketChange

    def __init__(self, quote_source_name: str, regular_market_open: PostMarketChange, average_daily_volume3_month: AverageDailyVolume10Day, exchange: str, regular_market_time: int, volume24_hr: DividendDate, regular_market_day_high: PostMarketChange, short_name: str, average_daily_volume10_day: AverageDailyVolume10Day, long_name: str, regular_market_change: PostMarketChange, currency_symbol: str, regular_market_previous_close: PostMarketChange, post_market_time: int, pre_market_price: DividendDate, exchange_data_delayed_by: int, to_currency: None, post_market_change: PostMarketChange, post_market_price: PostMarketChange, exchange_name: str, pre_market_change: DividendDate, circulating_supply: DividendDate, regular_market_day_low: PostMarketChange, price_hint: AverageDailyVolume10Day, currency: str, regular_market_price: PostMarketChange, regular_market_volume: AverageDailyVolume10Day, last_market: None, regular_market_source: str, open_interest: DividendDate, market_state: str, underlying_symbol: None, market_cap: AverageDailyVolume10Day, quote_type: str, volume_all_currencies: DividendDate, post_market_source: str, strike_price: DividendDate, symbol: str, post_market_change_percent: PostMarketChange, pre_market_source: str, max_age: int, from_currency: None, regular_market_change_percent: PostMarketChange) -> None:
        self.quote_source_name = quote_source_name
        self.regular_market_open = regular_market_open
        self.average_daily_volume3_month = average_daily_volume3_month
        self.exchange = exchange
        self.regular_market_time = regular_market_time
        self.volume24_hr = volume24_hr
        self.regular_market_day_high = regular_market_day_high
        self.short_name = short_name
        self.average_daily_volume10_day = average_daily_volume10_day
        self.long_name = long_name
        self.regular_market_change = regular_market_change
        self.currency_symbol = currency_symbol
        self.regular_market_previous_close = regular_market_previous_close
        self.post_market_time = post_market_time
        self.pre_market_price = pre_market_price
        self.exchange_data_delayed_by = exchange_data_delayed_by
        self.to_currency = to_currency
        self.post_market_change = post_market_change
        self.post_market_price = post_market_price
        self.exchange_name = exchange_name
        self.pre_market_change = pre_market_change
        self.circulating_supply = circulating_supply
        self.regular_market_day_low = regular_market_day_low
        self.price_hint = price_hint
        self.currency = currency
        self.regular_market_price = regular_market_price
        self.regular_market_volume = regular_market_volume
        self.last_market = last_market
        self.regular_market_source = regular_market_source
        self.open_interest = open_interest
        self.market_state = market_state
        self.underlying_symbol = underlying_symbol
        self.market_cap = market_cap
        self.quote_type = quote_type
        self.volume_all_currencies = volume_all_currencies
        self.post_market_source = post_market_source
        self.strike_price = strike_price
        self.symbol = symbol
        self.post_market_change_percent = post_market_change_percent
        self.pre_market_source = pre_market_source
        self.max_age = max_age
        self.from_currency = from_currency
        self.regular_market_change_percent = regular_market_change_percent

    @staticmethod
    def from_dict(obj: Any) -> 'Price':
        assert isinstance(obj, dict)
        quote_source_name = from_str(obj.get("quoteSourceName"))
        regular_market_open = PostMarketChange.from_dict(obj.get("regularMarketOpen"))
        average_daily_volume3_month = AverageDailyVolume10Day.from_dict(obj.get("averageDailyVolume3Month"))
        exchange = from_str(obj.get("exchange"))
        regular_market_time = from_int(obj.get("regularMarketTime"))
        volume24_hr = DividendDate.from_dict(obj.get("volume24Hr"))
        regular_market_day_high = PostMarketChange.from_dict(obj.get("regularMarketDayHigh"))
        short_name = from_str(obj.get("shortName"))
        average_daily_volume10_day = AverageDailyVolume10Day.from_dict(obj.get("averageDailyVolume10Day"))
        long_name = from_str(obj.get("longName"))
        regular_market_change = PostMarketChange.from_dict(obj.get("regularMarketChange"))
        currency_symbol = from_str(obj.get("currencySymbol"))
        regular_market_previous_close = PostMarketChange.from_dict(obj.get("regularMarketPreviousClose"))
        post_market_time = from_int(obj.get("postMarketTime"))
        pre_market_price = DividendDate.from_dict(obj.get("preMarketPrice"))
        exchange_data_delayed_by = from_int(obj.get("exchangeDataDelayedBy"))
        to_currency = from_none(obj.get("toCurrency"))
        post_market_change = PostMarketChange.from_dict(obj.get("postMarketChange"))
        post_market_price = PostMarketChange.from_dict(obj.get("postMarketPrice"))
        exchange_name = from_str(obj.get("exchangeName"))
        pre_market_change = DividendDate.from_dict(obj.get("preMarketChange"))
        circulating_supply = DividendDate.from_dict(obj.get("circulatingSupply"))
        regular_market_day_low = PostMarketChange.from_dict(obj.get("regularMarketDayLow"))
        price_hint = AverageDailyVolume10Day.from_dict(obj.get("priceHint"))
        currency = from_str(obj.get("currency"))
        regular_market_price = PostMarketChange.from_dict(obj.get("regularMarketPrice"))
        regular_market_volume = AverageDailyVolume10Day.from_dict(obj.get("regularMarketVolume"))
        last_market = from_none(obj.get("lastMarket"))
        regular_market_source = from_str(obj.get("regularMarketSource"))
        open_interest = DividendDate.from_dict(obj.get("openInterest"))
        market_state = from_str(obj.get("marketState"))
        underlying_symbol = from_none(obj.get("underlyingSymbol"))
        market_cap = AverageDailyVolume10Day.from_dict(obj.get("marketCap"))
        quote_type = from_str(obj.get("quoteType"))
        volume_all_currencies = DividendDate.from_dict(obj.get("volumeAllCurrencies"))
        post_market_source = from_str(obj.get("postMarketSource"))
        strike_price = DividendDate.from_dict(obj.get("strikePrice"))
        symbol = from_str(obj.get("symbol"))
        post_market_change_percent = PostMarketChange.from_dict(obj.get("postMarketChangePercent"))
        pre_market_source = from_str(obj.get("preMarketSource"))
        max_age = from_int(obj.get("maxAge"))
        from_currency = from_none(obj.get("fromCurrency"))
        regular_market_change_percent = PostMarketChange.from_dict(obj.get("regularMarketChangePercent"))
        return Price(quote_source_name, regular_market_open, average_daily_volume3_month, exchange, regular_market_time, volume24_hr, regular_market_day_high, short_name, average_daily_volume10_day, long_name, regular_market_change, currency_symbol, regular_market_previous_close, post_market_time, pre_market_price, exchange_data_delayed_by, to_currency, post_market_change, post_market_price, exchange_name, pre_market_change, circulating_supply, regular_market_day_low, price_hint, currency, regular_market_price, regular_market_volume, last_market, regular_market_source, open_interest, market_state, underlying_symbol, market_cap, quote_type, volume_all_currencies, post_market_source, strike_price, symbol, post_market_change_percent, pre_market_source, max_age, from_currency, regular_market_change_percent)

    def to_dict(self) -> dict:
        result: dict = {}
        result["quoteSourceName"] = from_str(self.quote_source_name)
        result["regularMarketOpen"] = to_class(PostMarketChange, self.regular_market_open)
        result["averageDailyVolume3Month"] = to_class(AverageDailyVolume10Day, self.average_daily_volume3_month)
        result["exchange"] = from_str(self.exchange)
        result["regularMarketTime"] = from_int(self.regular_market_time)
        result["volume24Hr"] = to_class(DividendDate, self.volume24_hr)
        result["regularMarketDayHigh"] = to_class(PostMarketChange, self.regular_market_day_high)
        result["shortName"] = from_str(self.short_name)
        result["averageDailyVolume10Day"] = to_class(AverageDailyVolume10Day, self.average_daily_volume10_day)
        result["longName"] = from_str(self.long_name)
        result["regularMarketChange"] = to_class(PostMarketChange, self.regular_market_change)
        result["currencySymbol"] = from_str(self.currency_symbol)
        result["regularMarketPreviousClose"] = to_class(PostMarketChange, self.regular_market_previous_close)
        result["postMarketTime"] = from_int(self.post_market_time)
        result["preMarketPrice"] = to_class(DividendDate, self.pre_market_price)
        result["exchangeDataDelayedBy"] = from_int(self.exchange_data_delayed_by)
        result["toCurrency"] = from_none(self.to_currency)
        result["postMarketChange"] = to_class(PostMarketChange, self.post_market_change)
        result["postMarketPrice"] = to_class(PostMarketChange, self.post_market_price)
        result["exchangeName"] = from_str(self.exchange_name)
        result["preMarketChange"] = to_class(DividendDate, self.pre_market_change)
        result["circulatingSupply"] = to_class(DividendDate, self.circulating_supply)
        result["regularMarketDayLow"] = to_class(PostMarketChange, self.regular_market_day_low)
        result["priceHint"] = to_class(AverageDailyVolume10Day, self.price_hint)
        result["currency"] = from_str(self.currency)
        result["regularMarketPrice"] = to_class(PostMarketChange, self.regular_market_price)
        result["regularMarketVolume"] = to_class(AverageDailyVolume10Day, self.regular_market_volume)
        result["lastMarket"] = from_none(self.last_market)
        result["regularMarketSource"] = from_str(self.regular_market_source)
        result["openInterest"] = to_class(DividendDate, self.open_interest)
        result["marketState"] = from_str(self.market_state)
        result["underlyingSymbol"] = from_none(self.underlying_symbol)
        result["marketCap"] = to_class(AverageDailyVolume10Day, self.market_cap)
        result["quoteType"] = from_str(self.quote_type)
        result["volumeAllCurrencies"] = to_class(DividendDate, self.volume_all_currencies)
        result["postMarketSource"] = from_str(self.post_market_source)
        result["strikePrice"] = to_class(DividendDate, self.strike_price)
        result["symbol"] = from_str(self.symbol)
        result["postMarketChangePercent"] = to_class(PostMarketChange, self.post_market_change_percent)
        result["preMarketSource"] = from_str(self.pre_market_source)
        result["maxAge"] = from_int(self.max_age)
        result["fromCurrency"] = from_none(self.from_currency)
        result["regularMarketChangePercent"] = to_class(PostMarketChange, self.regular_market_change_percent)
        return result


class QuoteType:
    exchange: str
    short_name: str
    long_name: str
    exchange_timezone_name: str
    exchange_timezone_short_name: str
    is_esg_populated: bool
    gmt_off_set_milliseconds: int
    quote_type: str
    symbol: str
    message_board_id: str
    market: str

    def __init__(self, exchange: str, short_name: str, long_name: str, exchange_timezone_name: str, exchange_timezone_short_name: str, is_esg_populated: bool, gmt_off_set_milliseconds: int, quote_type: str, symbol: str, message_board_id: str, market: str) -> None:
        self.exchange = exchange
        self.short_name = short_name
        self.long_name = long_name
        self.exchange_timezone_name = exchange_timezone_name
        self.exchange_timezone_short_name = exchange_timezone_short_name
        self.is_esg_populated = is_esg_populated
        self.gmt_off_set_milliseconds = gmt_off_set_milliseconds
        self.quote_type = quote_type
        self.symbol = symbol
        self.message_board_id = message_board_id
        self.market = market

    @staticmethod
    def from_dict(obj: Any) -> 'QuoteType':
        assert isinstance(obj, dict)
        exchange = from_str(obj.get("exchange"))
        short_name = from_str(obj.get("shortName"))
        long_name = from_str(obj.get("longName"))
        exchange_timezone_name = from_str(obj.get("exchangeTimezoneName"))
        exchange_timezone_short_name = from_str(obj.get("exchangeTimezoneShortName"))
        is_esg_populated = from_bool(obj.get("isEsgPopulated"))
        gmt_off_set_milliseconds = int(from_str(obj.get("gmtOffSetMilliseconds")))
        quote_type = from_str(obj.get("quoteType"))
        symbol = from_str(obj.get("symbol"))
        message_board_id = from_str(obj.get("messageBoardId"))
        market = from_str(obj.get("market"))
        return QuoteType(exchange, short_name, long_name, exchange_timezone_name, exchange_timezone_short_name, is_esg_populated, gmt_off_set_milliseconds, quote_type, symbol, message_board_id, market)

    def to_dict(self) -> dict:
        result: dict = {}
        result["exchange"] = from_str(self.exchange)
        result["shortName"] = from_str(self.short_name)
        result["longName"] = from_str(self.long_name)
        result["exchangeTimezoneName"] = from_str(self.exchange_timezone_name)
        result["exchangeTimezoneShortName"] = from_str(self.exchange_timezone_short_name)
        result["isEsgPopulated"] = from_bool(self.is_esg_populated)
        result["gmtOffSetMilliseconds"] = from_str(str(self.gmt_off_set_milliseconds))
        result["quoteType"] = from_str(self.quote_type)
        result["symbol"] = from_str(self.symbol)
        result["messageBoardId"] = from_str(self.message_board_id)
        result["market"] = from_str(self.market)
        return result


class TypeEnum(Enum):
    THE_10_K = "10-K"
    THE_10_Q = "10-Q"
    THE_8_K = "8-K"


class Filing:
    date: datetime
    epoch_date: int
    type: TypeEnum
    title: str
    edgar_url: str
    max_age: int

    def __init__(self, date: datetime, epoch_date: int, type: TypeEnum, title: str, edgar_url: str, max_age: int) -> None:
        self.date = date
        self.epoch_date = epoch_date
        self.type = type
        self.title = title
        self.edgar_url = edgar_url
        self.max_age = max_age

    @staticmethod
    def from_dict(obj: Any) -> 'Filing':
        assert isinstance(obj, dict)
        date = from_datetime(obj.get("date"))
        epoch_date = from_int(obj.get("epochDate"))
        type = TypeEnum(obj.get("type"))
        title = from_str(obj.get("title"))
        edgar_url = from_str(obj.get("edgarUrl"))
        max_age = from_int(obj.get("maxAge"))
        return Filing(date, epoch_date, type, title, edgar_url, max_age)

    def to_dict(self) -> dict:
        result: dict = {}
        result["date"] = self.date.isoformat()
        result["epochDate"] = from_int(self.epoch_date)
        result["type"] = to_enum(TypeEnum, self.type)
        result["title"] = from_str(self.title)
        result["edgarUrl"] = from_str(self.edgar_url)
        result["maxAge"] = from_int(self.max_age)
        return result


class SECFilings:
    filings: List[Filing]
    max_age: int

    def __init__(self, filings: List[Filing], max_age: int) -> None:
        self.filings = filings
        self.max_age = max_age

    @staticmethod
    def from_dict(obj: Any) -> 'SECFilings':
        assert isinstance(obj, dict)
        filings = from_list(Filing.from_dict, obj.get("filings"))
        max_age = from_int(obj.get("maxAge"))
        return SECFilings(filings, max_age)

    def to_dict(self) -> dict:
        result: dict = {}
        result["filings"] = from_list(lambda x: to_class(Filing, x), self.filings)
        result["maxAge"] = from_int(self.max_age)
        return result


class SummaryDetail:
    previous_close: PostMarketChange
    regular_market_open: PostMarketChange
    two_hundred_day_average: PostMarketChange
    trailing_annual_dividend_yield: DividendDate
    payout_ratio: PostMarketChange
    volume24_hr: DividendDate
    regular_market_day_high: PostMarketChange
    nav_price: DividendDate
    average_daily_volume10_day: AverageDailyVolume10Day
    total_assets: DividendDate
    regular_market_previous_close: PostMarketChange
    fifty_day_average: PostMarketChange
    trailing_annual_dividend_rate: DividendDate
    open: PostMarketChange
    to_currency: None
    average_volume10_days: AverageDailyVolume10Day
    expire_date: DividendDate
    summary_detail_yield: DividendDate
    algorithm: None
    dividend_rate: DividendDate
    ex_dividend_date: DividendDate
    beta: PostMarketChange
    circulating_supply: DividendDate
    start_date: DividendDate
    regular_market_day_low: PostMarketChange
    price_hint: AverageDailyVolume10Day
    currency: str
    trailing_pe: PostMarketChange
    regular_market_volume: AverageDailyVolume10Day
    last_market: None
    max_supply: DividendDate
    open_interest: DividendDate
    market_cap: AverageDailyVolume10Day
    volume_all_currencies: DividendDate
    strike_price: DividendDate
    average_volume: AverageDailyVolume10Day
    price_to_sales_trailing12_months: PostMarketChange
    day_low: PostMarketChange
    ask: PostMarketChange
    ytd_return: DividendDate
    ask_size: AverageDailyVolume10Day
    volume: AverageDailyVolume10Day
    fifty_two_week_high: PostMarketChange
    forward_pe: PostMarketChange
    max_age: int
    from_currency: None
    five_year_avg_dividend_yield: DividendDate
    fifty_two_week_low: PostMarketChange
    bid: PostMarketChange
    tradeable: bool
    dividend_yield: DividendDate
    bid_size: AverageDailyVolume10Day
    day_high: PostMarketChange

    def __init__(self, previous_close: PostMarketChange, regular_market_open: PostMarketChange, two_hundred_day_average: PostMarketChange, trailing_annual_dividend_yield: DividendDate, payout_ratio: PostMarketChange, volume24_hr: DividendDate, regular_market_day_high: PostMarketChange, nav_price: DividendDate, average_daily_volume10_day: AverageDailyVolume10Day, total_assets: DividendDate, regular_market_previous_close: PostMarketChange, fifty_day_average: PostMarketChange, trailing_annual_dividend_rate: DividendDate, open: PostMarketChange, to_currency: None, average_volume10_days: AverageDailyVolume10Day, expire_date: DividendDate, summary_detail_yield: DividendDate, algorithm: None, dividend_rate: DividendDate, ex_dividend_date: DividendDate, beta: PostMarketChange, circulating_supply: DividendDate, start_date: DividendDate, regular_market_day_low: PostMarketChange, price_hint: AverageDailyVolume10Day, currency: str, trailing_pe: PostMarketChange, regular_market_volume: AverageDailyVolume10Day, last_market: None, max_supply: DividendDate, open_interest: DividendDate, market_cap: AverageDailyVolume10Day, volume_all_currencies: DividendDate, strike_price: DividendDate, average_volume: AverageDailyVolume10Day, price_to_sales_trailing12_months: PostMarketChange, day_low: PostMarketChange, ask: PostMarketChange, ytd_return: DividendDate, ask_size: AverageDailyVolume10Day, volume: AverageDailyVolume10Day, fifty_two_week_high: PostMarketChange, forward_pe: PostMarketChange, max_age: int, from_currency: None, five_year_avg_dividend_yield: DividendDate, fifty_two_week_low: PostMarketChange, bid: PostMarketChange, tradeable: bool, dividend_yield: DividendDate, bid_size: AverageDailyVolume10Day, day_high: PostMarketChange) -> None:
        self.previous_close = previous_close
        self.regular_market_open = regular_market_open
        self.two_hundred_day_average = two_hundred_day_average
        self.trailing_annual_dividend_yield = trailing_annual_dividend_yield
        self.payout_ratio = payout_ratio
        self.volume24_hr = volume24_hr
        self.regular_market_day_high = regular_market_day_high
        self.nav_price = nav_price
        self.average_daily_volume10_day = average_daily_volume10_day
        self.total_assets = total_assets
        self.regular_market_previous_close = regular_market_previous_close
        self.fifty_day_average = fifty_day_average
        self.trailing_annual_dividend_rate = trailing_annual_dividend_rate
        self.open = open
        self.to_currency = to_currency
        self.average_volume10_days = average_volume10_days
        self.expire_date = expire_date
        self.summary_detail_yield = summary_detail_yield
        self.algorithm = algorithm
        self.dividend_rate = dividend_rate
        self.ex_dividend_date = ex_dividend_date
        self.beta = beta
        self.circulating_supply = circulating_supply
        self.start_date = start_date
        self.regular_market_day_low = regular_market_day_low
        self.price_hint = price_hint
        self.currency = currency
        self.trailing_pe = trailing_pe
        self.regular_market_volume = regular_market_volume
        self.last_market = last_market
        self.max_supply = max_supply
        self.open_interest = open_interest
        self.market_cap = market_cap
        self.volume_all_currencies = volume_all_currencies
        self.strike_price = strike_price
        self.average_volume = average_volume
        self.price_to_sales_trailing12_months = price_to_sales_trailing12_months
        self.day_low = day_low
        self.ask = ask
        self.ytd_return = ytd_return
        self.ask_size = ask_size
        self.volume = volume
        self.fifty_two_week_high = fifty_two_week_high
        self.forward_pe = forward_pe
        self.max_age = max_age
        self.from_currency = from_currency
        self.five_year_avg_dividend_yield = five_year_avg_dividend_yield
        self.fifty_two_week_low = fifty_two_week_low
        self.bid = bid
        self.tradeable = tradeable
        self.dividend_yield = dividend_yield
        self.bid_size = bid_size
        self.day_high = day_high

    @staticmethod
    def from_dict(obj: Any) -> 'SummaryDetail':
        assert isinstance(obj, dict)
        previous_close = PostMarketChange.from_dict(obj.get("previousClose"))
        regular_market_open = PostMarketChange.from_dict(obj.get("regularMarketOpen"))
        two_hundred_day_average = PostMarketChange.from_dict(obj.get("twoHundredDayAverage"))
        trailing_annual_dividend_yield = DividendDate.from_dict(obj.get("trailingAnnualDividendYield"))
        payout_ratio = PostMarketChange.from_dict(obj.get("payoutRatio"))
        volume24_hr = DividendDate.from_dict(obj.get("volume24Hr"))
        regular_market_day_high = PostMarketChange.from_dict(obj.get("regularMarketDayHigh"))
        nav_price = DividendDate.from_dict(obj.get("navPrice"))
        average_daily_volume10_day = AverageDailyVolume10Day.from_dict(obj.get("averageDailyVolume10Day"))
        total_assets = DividendDate.from_dict(obj.get("totalAssets"))
        regular_market_previous_close = PostMarketChange.from_dict(obj.get("regularMarketPreviousClose"))
        fifty_day_average = PostMarketChange.from_dict(obj.get("fiftyDayAverage"))
        trailing_annual_dividend_rate = DividendDate.from_dict(obj.get("trailingAnnualDividendRate"))
        open = PostMarketChange.from_dict(obj.get("open"))
        to_currency = from_none(obj.get("toCurrency"))
        average_volume10_days = AverageDailyVolume10Day.from_dict(obj.get("averageVolume10days"))
        expire_date = DividendDate.from_dict(obj.get("expireDate"))
        summary_detail_yield = DividendDate.from_dict(obj.get("yield"))
        algorithm = from_none(obj.get("algorithm"))
        dividend_rate = DividendDate.from_dict(obj.get("dividendRate"))
        ex_dividend_date = DividendDate.from_dict(obj.get("exDividendDate"))
        beta = PostMarketChange.from_dict(obj.get("beta"))
        circulating_supply = DividendDate.from_dict(obj.get("circulatingSupply"))
        start_date = DividendDate.from_dict(obj.get("startDate"))
        regular_market_day_low = PostMarketChange.from_dict(obj.get("regularMarketDayLow"))
        price_hint = AverageDailyVolume10Day.from_dict(obj.get("priceHint"))
        currency = from_str(obj.get("currency"))
        trailing_pe = PostMarketChange.from_dict(obj.get("trailingPE"))
        regular_market_volume = AverageDailyVolume10Day.from_dict(obj.get("regularMarketVolume"))
        last_market = from_none(obj.get("lastMarket"))
        max_supply = DividendDate.from_dict(obj.get("maxSupply"))
        open_interest = DividendDate.from_dict(obj.get("openInterest"))
        market_cap = AverageDailyVolume10Day.from_dict(obj.get("marketCap"))
        volume_all_currencies = DividendDate.from_dict(obj.get("volumeAllCurrencies"))
        strike_price = DividendDate.from_dict(obj.get("strikePrice"))
        average_volume = AverageDailyVolume10Day.from_dict(obj.get("averageVolume"))
        price_to_sales_trailing12_months = PostMarketChange.from_dict(obj.get("priceToSalesTrailing12Months"))
        day_low = PostMarketChange.from_dict(obj.get("dayLow"))
        ask = PostMarketChange.from_dict(obj.get("ask"))
        ytd_return = DividendDate.from_dict(obj.get("ytdReturn"))
        ask_size = AverageDailyVolume10Day.from_dict(obj.get("askSize"))
        volume = AverageDailyVolume10Day.from_dict(obj.get("volume"))
        fifty_two_week_high = PostMarketChange.from_dict(obj.get("fiftyTwoWeekHigh"))
        forward_pe = PostMarketChange.from_dict(obj.get("forwardPE"))
        max_age = from_int(obj.get("maxAge"))
        from_currency = from_none(obj.get("fromCurrency"))
        five_year_avg_dividend_yield = DividendDate.from_dict(obj.get("fiveYearAvgDividendYield"))
        fifty_two_week_low = PostMarketChange.from_dict(obj.get("fiftyTwoWeekLow"))
        bid = PostMarketChange.from_dict(obj.get("bid"))
        tradeable = from_bool(obj.get("tradeable"))
        dividend_yield = DividendDate.from_dict(obj.get("dividendYield"))
        bid_size = AverageDailyVolume10Day.from_dict(obj.get("bidSize"))
        day_high = PostMarketChange.from_dict(obj.get("dayHigh"))
        return SummaryDetail(previous_close, regular_market_open, two_hundred_day_average, trailing_annual_dividend_yield, payout_ratio, volume24_hr, regular_market_day_high, nav_price, average_daily_volume10_day, total_assets, regular_market_previous_close, fifty_day_average, trailing_annual_dividend_rate, open, to_currency, average_volume10_days, expire_date, summary_detail_yield, algorithm, dividend_rate, ex_dividend_date, beta, circulating_supply, start_date, regular_market_day_low, price_hint, currency, trailing_pe, regular_market_volume, last_market, max_supply, open_interest, market_cap, volume_all_currencies, strike_price, average_volume, price_to_sales_trailing12_months, day_low, ask, ytd_return, ask_size, volume, fifty_two_week_high, forward_pe, max_age, from_currency, five_year_avg_dividend_yield, fifty_two_week_low, bid, tradeable, dividend_yield, bid_size, day_high)

    def to_dict(self) -> dict:
        result: dict = {}
        result["previousClose"] = to_class(PostMarketChange, self.previous_close)
        result["regularMarketOpen"] = to_class(PostMarketChange, self.regular_market_open)
        result["twoHundredDayAverage"] = to_class(PostMarketChange, self.two_hundred_day_average)
        result["trailingAnnualDividendYield"] = to_class(DividendDate, self.trailing_annual_dividend_yield)
        result["payoutRatio"] = to_class(PostMarketChange, self.payout_ratio)
        result["volume24Hr"] = to_class(DividendDate, self.volume24_hr)
        result["regularMarketDayHigh"] = to_class(PostMarketChange, self.regular_market_day_high)
        result["navPrice"] = to_class(DividendDate, self.nav_price)
        result["averageDailyVolume10Day"] = to_class(AverageDailyVolume10Day, self.average_daily_volume10_day)
        result["totalAssets"] = to_class(DividendDate, self.total_assets)
        result["regularMarketPreviousClose"] = to_class(PostMarketChange, self.regular_market_previous_close)
        result["fiftyDayAverage"] = to_class(PostMarketChange, self.fifty_day_average)
        result["trailingAnnualDividendRate"] = to_class(DividendDate, self.trailing_annual_dividend_rate)
        result["open"] = to_class(PostMarketChange, self.open)
        result["toCurrency"] = from_none(self.to_currency)
        result["averageVolume10days"] = to_class(AverageDailyVolume10Day, self.average_volume10_days)
        result["expireDate"] = to_class(DividendDate, self.expire_date)
        result["yield"] = to_class(DividendDate, self.summary_detail_yield)
        result["algorithm"] = from_none(self.algorithm)
        result["dividendRate"] = to_class(DividendDate, self.dividend_rate)
        result["exDividendDate"] = to_class(DividendDate, self.ex_dividend_date)
        result["beta"] = to_class(PostMarketChange, self.beta)
        result["circulatingSupply"] = to_class(DividendDate, self.circulating_supply)
        result["startDate"] = to_class(DividendDate, self.start_date)
        result["regularMarketDayLow"] = to_class(PostMarketChange, self.regular_market_day_low)
        result["priceHint"] = to_class(AverageDailyVolume10Day, self.price_hint)
        result["currency"] = from_str(self.currency)
        result["trailingPE"] = to_class(PostMarketChange, self.trailing_pe)
        result["regularMarketVolume"] = to_class(AverageDailyVolume10Day, self.regular_market_volume)
        result["lastMarket"] = from_none(self.last_market)
        result["maxSupply"] = to_class(DividendDate, self.max_supply)
        result["openInterest"] = to_class(DividendDate, self.open_interest)
        result["marketCap"] = to_class(AverageDailyVolume10Day, self.market_cap)
        result["volumeAllCurrencies"] = to_class(DividendDate, self.volume_all_currencies)
        result["strikePrice"] = to_class(DividendDate, self.strike_price)
        result["averageVolume"] = to_class(AverageDailyVolume10Day, self.average_volume)
        result["priceToSalesTrailing12Months"] = to_class(PostMarketChange, self.price_to_sales_trailing12_months)
        result["dayLow"] = to_class(PostMarketChange, self.day_low)
        result["ask"] = to_class(PostMarketChange, self.ask)
        result["ytdReturn"] = to_class(DividendDate, self.ytd_return)
        result["askSize"] = to_class(AverageDailyVolume10Day, self.ask_size)
        result["volume"] = to_class(AverageDailyVolume10Day, self.volume)
        result["fiftyTwoWeekHigh"] = to_class(PostMarketChange, self.fifty_two_week_high)
        result["forwardPE"] = to_class(PostMarketChange, self.forward_pe)
        result["maxAge"] = from_int(self.max_age)
        result["fromCurrency"] = from_none(self.from_currency)
        result["fiveYearAvgDividendYield"] = to_class(DividendDate, self.five_year_avg_dividend_yield)
        result["fiftyTwoWeekLow"] = to_class(PostMarketChange, self.fifty_two_week_low)
        result["bid"] = to_class(PostMarketChange, self.bid)
        result["tradeable"] = from_bool(self.tradeable)
        result["dividendYield"] = to_class(DividendDate, self.dividend_yield)
        result["bidSize"] = to_class(AverageDailyVolume10Day, self.bid_size)
        result["dayHigh"] = to_class(PostMarketChange, self.day_high)
        return result


class Welcome:
    financials_template: FinancialsTemplate
    price: Price
    sec_filings: SECFilings
    quote_type: QuoteType
    calendar_events: CalendarEvents
    summary_detail: SummaryDetail
    symbol: str
    asset_profile: AssetProfile
    page_views: PageViews

    def __init__(self, financials_template: FinancialsTemplate, price: Price, sec_filings: SECFilings, quote_type: QuoteType, calendar_events: CalendarEvents, summary_detail: SummaryDetail, symbol: str, asset_profile: AssetProfile, page_views: PageViews) -> None:
        self.financials_template = financials_template
        self.price = price
        self.sec_filings = sec_filings
        self.quote_type = quote_type
        self.calendar_events = calendar_events
        self.summary_detail = summary_detail
        self.symbol = symbol
        self.asset_profile = asset_profile
        self.page_views = page_views

    @staticmethod
    def from_dict(obj: Any) -> 'Welcome':
        assert isinstance(obj, dict)
        financials_template = FinancialsTemplate.from_dict(obj.get("financialsTemplate"))
        price = Price.from_dict(obj.get("price"))
        sec_filings = SECFilings.from_dict(obj.get("secFilings"))
        quote_type = QuoteType.from_dict(obj.get("quoteType"))
        calendar_events = CalendarEvents.from_dict(obj.get("calendarEvents"))
        summary_detail = SummaryDetail.from_dict(obj.get("summaryDetail"))
        symbol = from_str(obj.get("symbol"))
        asset_profile = AssetProfile.from_dict(obj.get("assetProfile"))
        page_views = PageViews.from_dict(obj.get("pageViews"))
        return Welcome(financials_template, price, sec_filings, quote_type, calendar_events, summary_detail, symbol, asset_profile, page_views)

    def to_dict(self) -> dict:
        result: dict = {}
        result["financialsTemplate"] = to_class(FinancialsTemplate, self.financials_template)
        result["price"] = to_class(Price, self.price)
        result["secFilings"] = to_class(SECFilings, self.sec_filings)
        result["quoteType"] = to_class(QuoteType, self.quote_type)
        result["calendarEvents"] = to_class(CalendarEvents, self.calendar_events)
        result["summaryDetail"] = to_class(SummaryDetail, self.summary_detail)
        result["symbol"] = from_str(self.symbol)
        result["assetProfile"] = to_class(AssetProfile, self.asset_profile)
        result["pageViews"] = to_class(PageViews, self.page_views)
        return result


def welcome_from_dict(s: Any) -> Welcome:
    return Welcome.from_dict(s)


def welcome_to_dict(x: Welcome) -> Any:
    return to_class(Welcome, x)
