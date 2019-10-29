from django.http import JsonResponse
import requests
import settings
import time

from .forms import *

def createSession():
    session = requests.Session()
    response = session.get(url='https://edeedel.amocrm.ru/private/api/auth.php')

    r = session.post("https://edeedel.amocrm.ru/private/api/auth.php",
                     data={'USER_LOGIN': settings.AMO_EMAIL, 'USER_HASH': settings.AMO_KEY})
    print(r.status_code, r.reason)
    print(session.cookies.get_dict())
    print(response.status_code)
    return session


def createContact(session,name,phone,tags):
    NEWCONTACT = {
        'add': [{
            'name': name,
            'created_at': time.time(),
            'tags': tags,

            'custom_fields': [
                {
                    'id': "85861",
                    'values': [{
                        'value': phone,
                        'enum': "WORK"
                    },
                    ]
                },
            ]
        }]
    }
    r = session.post("https://edeedel.amocrm.ru/api/v2/contacts", json=NEWCONTACT)

    return r.json()['_embedded']['items'][0]['id']


def createLead(session,userid,lead_type):
    JSONFORMDATA = {

        'add': [{
            'name': lead_type,
            'created_at': time.time(),
            'updated_a': "1508274000",
            'status_id': "13670637",

            'tags': "запрос, звонок",
            'contacts_id': [
                userid
            ],
            'company_id': "1099148",
            'catalog_elements_id': {
                99999: {
                    111111: 10
                }
            },
            'custom_fields': [{
                'id': "4399649",
                'values': [
                    "3691615",
                    "3691616",
                    "3691617"
                ]
            },

                {
                    'id': "3691615",
                    'values': [{
                        'value': "ул. Охотный ряд, 1",
                        'subtype': "address_line_1"
                    },
                        {
                            'value': "Москва",
                            'subtype': "city"
                        }

                    ]
                }
            ]
        }]
    }

    r = session.post("https://edeedel.amocrm.ru/api/v2/leads", json=JSONFORMDATA)
    print(r.status_code, r.reason)



def createCallbackForm(request):
    print(request.POST)
    return_dict = {}
    if request.POST:
        form = CallbackForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return_dict['result'] = 'ok'
        else:
            return_dict['result'] = 'error'
            return_dict['errors'] = form.errors
            print(form.errors)

    return JsonResponse(return_dict)


def createCallbackOrderForm(request):
    return_dict = {}
    if request.POST:
        form = CallbackOrderForm(request.POST)
        if form.is_valid():
            name = request.POST.get('userName')
            phone = request.POST.get('userPhone')
            form.save()
            return_dict['result'] = 'ok'
            createLead(createSession(),createContact(createSession(),name,phone,'запрос, обратный звонок'),'Обратный звонок')
        else:
            return_dict['result'] = 'error'
            return_dict['errors'] = form.errors
            print(form.errors)
    return JsonResponse(return_dict)