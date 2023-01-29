import config
import requests

ORDERS_URL = '{}/v2/orders'.format(config.ALPACA_BASE_URL)
def createMarketOrder(ticker, qty, side, type):
    data = {
        'symbol': ticker,
        'qty': qty,
        'side': side,
        'type': type,
        'time_in_force': 'gtc'
    }
    r.request.post(ORDERS_URL, json=data, headers=config.HEADERS)