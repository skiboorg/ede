import json

from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import *

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
    print(request.POST.get('orders'))
    req = request.POST.get('orders')

    for x in range(0,len(req)-1):
        print(req[x])
        print(req[x])
        x += 1

