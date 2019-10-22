from django.shortcuts import render
from service.models import *
from callback.forms import *

def index(request):
    callbackForm = CallbackForm()
    allService = ServiceName.objects.all()
    allSubjects = Subject.objects.all()
    return render(request, 'index/index.html', locals())
