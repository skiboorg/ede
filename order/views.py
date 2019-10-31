import base64
import json
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .forms import *
from order.models import Order
from customuser.models import UserLog

def newOrder(request):
    print(request.POST)

    if request.POST:
        form = OrderForm(request.POST, request.FILES)
        form.user_id = request.user.id
        if form.is_valid():
            form.save()
        else:
            print(form.errors)

        return HttpResponseRedirect('/lk')

def newMesage(request):
    print(request.POST)

    if request.POST:
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)

        return HttpResponseRedirect('/lk')

def decode(encodeString):
    params = encodeString.split('++')[1].split('==')
    pid = base64.b64decode(params[0]+'==').decode('utf-8') #тип оплаты 1 полная оплата,  0 предоплата
    print('pid',pid)
    id = base64.b64decode(params[1]+'==').decode('utf-8') #id заказа
    print('id', id)
    return (id,pid)

def pay(request):
    if request.POST:
        req = request.POST.get('orders')
        return_dict = {}
        totalprice = 0
        wallet = '41001887932830'
        targets = ''
        label= {}
        print(json.loads(req))
        ordersIds=[]

        for order in json.loads(req):

            encodeString = json.loads(req)[order]['id']
            id, pid = decode(encodeString)
            if not id in ordersIds:
                ordersIds.append(id)
                # pid = json.loads(req)[order]['pid'].split(':')[1][0] #pid = 1 полная оплата,  0 предоплата
                o = Order.objects.get(id=id)
                if pid == '1':
                    if not o.is_prePayed:
                        totalprice += o.fullPrice
                        targets += 'Оплата заказа № {};'.format(o.id)

                    else:
                        totalprice += o.fullPrice - o.prePay
                        targets += 'Доплата заказа № {};'.format(o.id)

                    label['{}'.format(o.id)] = pid
                elif pid == '0':
                    totalprice += o.prePay
                    targets += 'Предоплата заказа № {};'.format(o.id)
                    label['{}'.format(o.id)] = pid
                else:
                    UserLog.objects.create(user=request.user, action='Попытка подделки запроса')
                    return_dict['result'] = 'error'

                UserLog.objects.create(user=request.user, action='Попытка : {} на сумму {}'.format(targets, totalprice))
                return_dict['result'] = 'ok'
                return_dict['totalprice'] = totalprice
                return_dict['label'] = json.dumps(label)
                return_dict['wallet'] = wallet
                return_dict['targets'] = targets
            else:
                UserLog.objects.create(user=request.user, action='Попытка подделки запроса')
                return_dict['result'] = 'error'

        return JsonResponse(return_dict)


@csrf_exempt
def pay_complete(request):
    print(request.POST)
    notification_type = request.POST.get('notification_type')
    amount  = request.POST.get('amount')
    codepro  = request.POST.get('codepro')
    withdraw_amount  = request.POST.get('withdraw_amount')
    unaccepted  = request.POST.get('unaccepted')
    label  = request.POST.get('label')
    datetime  = request.POST.get('datetime')
    sender  = request.POST.get('sender')
    sha1_hash  = request.POST.get('sha1_hash')
    operation_id  = request.POST.get('operation_id')

    if not unaccepted or codepro:
        pass

    else:
        pass





