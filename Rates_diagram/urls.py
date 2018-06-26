from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^myChart/', views.myChart),
    # url(r'^newRates/', views.newRates),
    url(r'^', views.index),

]