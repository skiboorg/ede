from django.http import JsonResponse
from django.shortcuts import render

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
    print(request.POST)
    return_dict = {}
    if request.POST:
        form = CallbackOrderForm(request.POST)
        if form.is_valid():
            form.save()
            return_dict['result'] = 'ok'
        else:
            return_dict['result'] = 'error'
            return_dict['errors'] = form.errors
            print(form.errors)
    return JsonResponse(return_dict)