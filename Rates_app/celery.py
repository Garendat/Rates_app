# import os
# from celery import Celery
# from django.conf import settings
#
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Rates_app.settings')
#
# app = Celery('Rates_app')
#
# app.config_from_object('django.conf:settings')
#
# app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

import os
from celery import Celery
from celery.schedules import crontab
from  datetime import timedelta
# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Rates_app.settings')
from django.conf import settings  # noqa
app = Celery('Rates_app')
# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
app.conf.beat_schedule = {
    'send-report-every-single-minute': {
        'task': 'Rates_diagram.tasks.newRates',
        'schedule': timedelta(seconds=10),  # change to `crontab(minute=0, hour=0)` if you want it to run daily at midnight
    },
}