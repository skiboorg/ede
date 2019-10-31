import json
from django.http import HttpResponseRedirect
from django.http import JsonResponse
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


def pay(request):
    if request.POST:
        req = request.POST.get('orders')
        return_dict = {}
        totalprice = 0
        wallet = '41001887932830'
        targets = ''
        label= {}
        print(json.loads(req))

        for order in json.loads(req):
            id = json.loads(req)[order]['id']
            pid = json.loads(req)[order]['pid'].split(':')[1][0] #pid = 1 полная оплата,  0 предоплата
            o = Order.objects.get(id=id)
            if pid == '1':
                totalprice += o.fullPrice
                targets += 'Оплата заказа № {};'.format(o.id)
                label['orderId{}'.format(o.id)] = pid
            elif pid == '0':
                totalprice += o.prePay
                targets += 'Предоплата заказа № {};'.format(o.id)
                label['orderId{}'.format(o.id)] = pid
            else:
                pass
        UserLog.objects.create(user=request.user, action='Попытка : {} на сумму {}'.format(targets,totalprice))

        return_dict['totalprice']=totalprice
        return_dict['label'] = label
        return_dict['wallet'] = wallet
        return_dict['targets'] = targets
        return JsonResponse(return_dict)








