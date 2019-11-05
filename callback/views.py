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


def createContact(session,name,phone,email,tags):
    if not name:
        name = 'Не указано'

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
                {
                    'id': "85863",
                    'values': [{
                        'value': email,
                        'enum': "WORK"
                    },
                    ]
                },
            ]
        }]
    }
    print(name)
    print(phone)
    print(email)
    print(tags)
    r = session.post("https://edeedel.amocrm.ru/api/v2/contacts", json=NEWCONTACT)
    print(r.json())

    return r.json()['_embedded']['items'][0]['id']


def createLead(session,userid,lead_type,workType,subject,volume,deadline,about):
    JSONFORMDATA = {

        'add': [{
            'name': lead_type,
            'created_at': time.time(),
            'updated_a': "1508274000",
            'status_id': "13670637",

            'tags': lead_type,
            'contacts_id': [
                userid
            ],

            'custom_fields': [
                {
                    'id': "202121",
                    'values': [{
                        'value': workType,
                        'enum': "WORK"
                    },
                    ]
                },
                {
                    'id': "202123",
                    'values': [{
                        'value': about,
                        'enum': "WORK"
                    },
                    ]
                },
                {
                    'id': "202127",
                    'values': [{
                        'value': volume,
                        'enum': "WORK"
                    },
                    ]
                },
                {
                    'id': "202129",
                    'values': [{
                        'value': deadline,
                        'enum': "WORK"
                    },
                    ]
                }, {
                    'id': "202165",
                    'values': [{
                        'value': subject,
                        'enum': "WORK"
                    },
                    ]
                },
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
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            workName = request.POST.get('workName')
            subject = request.POST.get('subject')
            about = request.POST.get('about')
            email = request.POST.get('email')
            volume = request.POST.get('volume')
            deadLine = request.POST.get('deadLine')

            return_dict['result'] = 'ok'
            createLead(createSession(), createContact(createSession(), name, phone, email, 'расчет цены'),
                       'Расчет стоимости', workName, subject, volume, deadLine, about)
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
            createLead(createSession(),createContact(createSession(),name,phone,'Не указан','обратный звонок'),
                       'Обратный звонок','Не указан','Не указан','Не указан','Не указан','Не указан')
        else:
            return_dict['result'] = 'error'
            return_dict['errors'] = form.errors
            print(form.errors)
    return JsonResponse(return_dict)