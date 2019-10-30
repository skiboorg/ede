from django.shortcuts import render
import requests
import json
from yandex_money.api import Wallet, ExternalPayment
import settings
def yandex_auth():
    headers = {
        'Host': 'money.yandex.ru',
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'Content-Length': '154'
    }
    params = {
        'client_id': settings.YANDEX_CLIENT_ID,
        'response_type': 'code',
        'redirect_uri': 'http://localhost/lk',
        'scope': 'account-info'
    }
    r = requests.post(settings.YANDEX_API_URL,data=json(params),headers=headers)
    print(r)

def payRequest():
    pass
