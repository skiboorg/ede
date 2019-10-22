from django.shortcuts import render
from service.models import *
from callback.forms import *
from comments.models import *

def index(request):
    callbackForm = CallbackForm()
    allService = ServiceName.objects.all()
    allSubjects = Subject.objects.all()
    allComments = Comment.objects.all()
    return render(request, 'pages/index.html', locals())
def prices(request):
    callbackForm = CallbackForm()
    allService = ServiceName.objects.all()
    allSubjects = Subject.objects.all()
    return render(request, 'pages/prices.html', locals())

def contacts(request):
    callbackForm = CallbackForm()
    return render(request, 'pages/contacts.html', locals())