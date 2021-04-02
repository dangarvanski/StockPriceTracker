from Yahoo import YahooResponse


def map_asset_profile(price_text):
    assetProfile = YahooResponse.AssetProfile

    assetProfile.CompanyOfficers = price_text["companyOfficers"]
    assetProfile.Name = price_text["name"]
    assetProfile.StartDate = price_text["startDate"]
    assetProfile.Description = price_text["description"]
    assetProfile.MaxAge = price_text["maxAge"]

    return assetProfile
