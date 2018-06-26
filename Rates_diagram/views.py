from datetime import datetime

import requests
from django.http import JsonResponse
from django.shortcuts import render
from .models import Rates_all
# from .tasks import newRates


# Create your views here.


def index(request):
    item_name = ['DSHBTC', 'EMCBTC', 'BTCUSD', 'LTCUSD', 'EURUSD', 'GBPUSD', 'USDCNH', 'LTCRUB', 'EURJPY', 'USDJPY',
                 'USDCHF', 'USDRUB',
                 'AUDUSD', 'USDCAD', 'USDINR', 'LTCBTC', 'ETHBTC', 'ETHLTC', 'NMCBTC', 'PPCBTC']
    return render(request, 'Rates_diagram/Rates_diagram.html', {'item_name': item_name})


def myChart(request):
    if request.method == 'GET':
        name = request.GET.get('data')
        # date = request.GET.get('date')
        # print(name)
        # print(date)
        # time = 0
        # if date == 'today':
        #     time == datetime.today()
        # elif date == 'yesterday':
        #     time = datetime
        # elif date == 'two days ago':
        #     time = 0
        # else:
        #     time = datetime.today()
        # rates_date = Rates_all.objects.filter(created=time)
        rates_name = Rates_all.objects.filter(symbol=name)
        rates_bid = []
        rates_date = []
        for item in rates_name:
            rates_bid.append(item.bid)
            rates_date.append(item.created)
        data = {
            'bid': rates_bid,
            'date': rates_date,
        }
        return JsonResponse(data)





