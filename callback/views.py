from django.http import JsonResponse
import requests
import settings
import time

from .forms import *

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
    newuserID = 0
    return_dict = {}
    if request.POST:
        form = CallbackOrderForm(request.POST)
        if form.is_valid():
            form.save()
            return_dict['result'] = 'ok'

            NEWCONTACT = {
                'add': [{
                    'name': request.POST.get('userName') ,
                    'created_at': time.time(),
                    'tags': "заявка,обратный звонок",

                    'custom_fields': [
                        {
                            'id': "85861",
                            'values': [{
                                'value': request.POST.get('userPhone'),
                                'enum': "WORK"
                            },
                            ]
                        },


                    ]
                }]
            }



            session = requests.Session()
            response = session.get(url='https://edeedel.amocrm.ru/private/api/auth.php')
            print(request.POST)
            r = session.post("https://edeedel.amocrm.ru/private/api/auth.php",
                             data={'USER_LOGIN': settings.AMO_EMAIL, 'USER_HASH': settings.AMO_KEY})
            print(r.status_code, r.reason)
            print(session.cookies.get_dict())
            print(response.status_code)
            r = session.post("https://edeedel.amocrm.ru/api/v2/contacts", json=NEWCONTACT)

            newuserID = r.json()['_embedded']['items'][0]['id']
            print(newuserID)

            JSONFORMDATA = {

                'add': [{
                    'name': "Запрос на обратный звонок ",
                    'created_at': time.time(),
                    'updated_a': "1508274000",
                    'status_id': "13670637",

                    'tags': "запрос, звонок",
                    'contacts_id': [
                        newuserID
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

        else:
            return_dict['result'] = 'error'
            return_dict['errors'] = form.errors
            print(form.errors)
    return JsonResponse(return_dict)