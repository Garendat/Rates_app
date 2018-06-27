import requests
from Rates_app.celery import app

from .models import Rates_all


@app.task
def newRates():
    item_string = requests.get('https://cryptottlivewebapi.xbtce.net:8443/api/v1/public/level2')
    item_name = ['DSHBTC', 'EMCBTC', 'BTCUSD', 'LTCUSD', 'EURUSD', 'GBPUSD', 'USDCNH', 'LTCRUB', 'EURJPY', 'USDJPY',
                 'USDCHF', 'USDRUB',
                 'AUDUSD', 'USDCAD', 'USDINR', 'LTCBTC', 'ETHBTC', 'ETHLTC', 'NMCBTC', 'PPCBTC']
    for item in item_string.json():
        if item['Symbol'] in item_name:
            item['Symbol'] = Rates_all(symbol=item['Symbol'], bid=item['BestBid']['Price'],
                                       ask=item['BestBid']['Volume'])
            item['Symbol'].save()
    print('eeeeeeexyyyyyyyyyyyyyyy')
