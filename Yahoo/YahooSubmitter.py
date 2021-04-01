from Yahoo import YahooClient


def submit(request):
    request_obj = {"symbol": request.get_symbol(), "region": request.get_region()}

    response_obj = YahooClient.get_profile(request_obj)
    return response_obj
