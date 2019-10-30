import requests
import json
from yandex_money.api import Wallet, ExternalPayment
import settings

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
session = requests.Session()
r = session.post(settings.YANDEX_API_URL, data=params, headers=headers)
print(r.status_code)
print(r.reason)