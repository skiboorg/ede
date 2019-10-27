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

