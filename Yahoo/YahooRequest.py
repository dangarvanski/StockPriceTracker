class YahooRequest:
    def __init__(self, symbol='', region=''):
        self._symbol = symbol
        self._region = region

    # getter method
    def get_symbol(self):
        return self._symbol

    # setter method
    def set_symbol(self, x):
        self._symbol = x
    # getter method

    def get_region(self):
        return self._region

    # setter method
    def set_region(self, x):
        self._region = x