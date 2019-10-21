from django.shortcuts import render
from service.models import *

def index(request):
    allService = ServiceName.objects.all()
    allSubjects = Subject.objects.all()
    return render(request, 'index/index.html', locals())
