import base64
import json
from django.http import HttpResponseRedirect, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .forms import *
from order.models import Order, Payment
from customuser.models import UserLog
from callback.views import createSession,createContact,createLead

import settings

def newOrder(request):

    if request.POST:
        req = request.POST
        form = OrderForm(req, request.FILES)
        form.user_id = request.user.id
        if form.is_valid():
            form.save()
            name = request.user.name
            phone = request.user.phone
            workName = request.POST.get('workName')
            subject = request.POST.get('subject')
            volume = request.POST.get('volume')
            about = request.POST.get('about')
            email = request.user.email
            deadLine = request.POST.get('deadLine')
            createLead(createSession(), createContact(createSession(), name, phone, email, 'Новый заказ'),
                       'Новый заказ', workName, subject, volume, deadLine, about)
        else:
            print(form.errors)

        return HttpResponseRedirect('/lk')

def newMesage(request):

    if request.POST:
        req = request.POST
        form = MessageForm(req)
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


# notification_type=p2p-incoming&bill_id=&amount=12.94&codepro=false&withdraw_amount=13.00&unaccepted=false&label={"3": "0", "4": "1", "5": "0"}&datetime=2019-11-01T07:05:11Z&sender=410016706719303&sha1_hash=4805d7a4b758b6845118532b4444e59953b7fe85&operation_label=254decb7-0011-5000-a000-1b9c0b312388&operation_id=625907111593064008&currency=643




def pay(request):
    if request.POST:
        req = request.POST
        req = req.get('orders')
        return_dict = {}
        totalprice = 0
        wallet = settings.WALLET

        targets = ''
        label= {}
        print(json.loads(req))
        ordersIds=[]
        label['user'] = request.user.id
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
    if settings.DEV:
        req = request.GET
    else:
        req = request.POST
    notification_type = req.get('notification_type')
    amount = req.get('amount')
    codepro  = req.get('codepro')
    withdraw_amount = req.get('withdraw_amount')
    unaccepted = req.get('unaccepted')
    label = json.loads(req.get('label'))
    datetime  = req.get('datetime')
    sender = req.get('sender')
    sha1_hash = req.get('sha1_hash')
    operation_id = req.get('operation_id')
    payment_source = ''
    order = None
    user_id = 0

    if notification_type == 'p2p-incoming':
        payment_source = 'из кошелька'
    else:
        payment_source = 'c карты'
    if not unaccepted or codepro:
        for x in label:
            if x == 'user':
                user_id = int(label[x])
            else:
                order_id = x
                payment_type = label[x]

                try:
                    order = Order.objects.get(id=order_id)
                    print(order)
                except:
                    print('order not found')
                    UserLog.objects.create(user_id=user_id,
                                           action='Попытка оплаты не существуюшего заказа')
                    return HttpResponse(status=500)
                if order:
                    if payment_type == '0' and not order.is_prePayed:
                        order.is_prePayed = True
                        order.save(force_update=True)
                        print('order is prepay now')

                        UserLog.objects.create(user_id=user_id,
                                               action='Предоплата заказа {}'.format(order.id))

                        newPayment = Payment.objects.create(order=order,
                                               user_id=user_id,
                                               amount=amount,
                                               withdraw_amount=withdraw_amount,
                                               sender=sender,
                                               type='Предоплата {}'.format(payment_source),
                                               operation_id=operation_id)
                        print(newPayment)
                    else:
                        print('order is prepay already')
                    if payment_type == '1' and not order.is_fullPayed:
                        order.is_fullPayed = True
                        if order.is_prePayed:
                            payment_type_name = 'Доплата'
                        else:
                            payment_type_name = 'Оплата'
                        order.save(force_update=True)
                        print('order is payed now')
                        UserLog.objects.create(user_id=user_id,
                                               action='Оплата заказа {}'.format(order.id))
                        Payment.objects.create(order=order,
                                               user_id=user_id,
                                               amount=amount,
                                               withdraw_amount=withdraw_amount,
                                               sender=sender,
                                               type='{} {}'.format(payment_type_name, payment_source),
                                               operation_id=operation_id)

                    else:
                        print('order is payed already')

        return HttpResponse(status=200)
    else:
        UserLog.objects.create(user_id=user_id, action='Оплата не удалась, платеж  защищен кодом протекции или еще не проведен')
        return HttpResponse(status=500)








