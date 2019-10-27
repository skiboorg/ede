from django.shortcuts import render
from service.models import *
from callback.forms import *
from order.forms import *
from comments.models import *
from customuser.forms import UpdateForm
from order.models import Order
import random



def index(request):
    n1 = random.randint(0, 9)
    n2 = random.randint(0, 9)
    callbackForm = CallbackForm()
    callbackOrderForm = CallbackOrderForm()
    allService = ServiceName.objects.all()
    allSubjects = Subject.objects.all()
    allComments = Comment.objects.all()
    return render(request, 'pages/index.html', locals())
def prices(request):
    n1 = random.randint(0, 9)
    n2 = random.randint(0, 9)
    callbackForm = CallbackForm()
    callbackOrderForm = CallbackOrderForm()
    allService = ServiceName.objects.all()
    allSubjects = Subject.objects.all()
    return render(request, 'pages/prices.html', locals())

def contacts(request):
    n1 = random.randint(0, 9)
    n2 = random.randint(0, 9)
    callbackForm = CallbackForm()
    callbackOrderForm = CallbackOrderForm()
    return render(request, 'pages/contacts.html', locals())


def lk(request):
    n1 = random.randint(0, 9)
    n2 = random.randint(0, 9)
    if request.user.is_authenticated:
        messageForm = MessageForm()
        orderForm = OrderForm()
        userForm = UpdateForm()
        allOrders = Order.objects.filter(user=request.user, is_complete=False)
        allService = ServiceName.objects.all()
        allSubjects = Subject.objects.all()
        return render(request, 'pages/lk.html', locals())
    else:
        return render(request, 'pages/index.html', locals())