from django.urls import path

from . import views

#TODO: JSON URL interpretieren als Test
# curl -H 'Content-Type: application/json; charset=utf-8' -d '{"text": "BTCUSD Greater Than 9000"}' -X POST https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX

#Todo: weitere befehle aus Tradingview interpretieren

#todo: verbindung mit einer auth Kennzeichnung absichern

#todo: nur gewisse IP adressen erlauben

#todo nur https erlauben

#todo Request in eine Tabelle schreiben time, request and return, dauer

#todo: daraus resultierenden Profit in die Tabelle schreiben bei close



urlpatterns = [
    path('', views.index, name='index'),
]
