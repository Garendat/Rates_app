from datetime import datetime, timedelta

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
        date = request.GET.get('date')
        date_now = datetime.today()
        time = 0
        if date == 'today':
            time = date_now
        elif date == 'yesterday':
            time = date_now - timedelta(days=1)
        elif date == 'two_days_ago':
            time = date_now - timedelta(days=2)
        else:
            time = date_now
        rates_all = Rates_all.objects.all()
        rates_date = rates_all.filter(created__startswith=time.strftime('%Y-%m-%d'))
        rates_name = rates_date.filter(symbol=name)
        rates_bid = []
        rates_date = []
        for item in rates_name:
            rates_bid.append(item.bid)
            rates_date.append(item.created.strftime('%H.%M'))
        data = {
            'bid': rates_bid,
            'date': rates_date,
        }
        return JsonResponse(data)





