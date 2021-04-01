import requests

headers = {
    'x-rapidapi-key': "93b4c4cb9bmsh372692ef99145d4p1c9f8djsnec2e5d969ea7",
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
}


def get_profile(request):
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-profile"
    return requests.request("GET", url, headers=headers, params=request)
