import bs4
import requests
import json

class YahooAPICall:
    def get_websiteData(apiLink):
        websiteData = requests.get(apiLink)
        return bs4.BeautifulSoup(websiteData.text, 'html.parser')

    def get_updateData(apiLink):
        response = requests.get(apiLink)
        return response.text