from django.shortcuts import render
from django.http import HttpResponse
from service.models import *
from callback.forms import *
from order.forms import *
from comments.models import *
from blog.models import *
from customuser.forms import UpdateForm
from order.models import Order
import random
import settings



def index(request):
    n1 = random.randint(0, 9)
    n2 = random.randint(0, 9)
    callbackForm = CallbackForm()
    callbackOrderForm = CallbackOrderForm()
    allService = ServiceName.objects.all()
    allComments = Comment.objects.all()
    print('request.subdomain', request.subdomain)
    return render(request, 'pages/index.html', locals())

def robots(request):
    subdomain = request.subdomain
    if subdomain:
        robotsTxt = "User-agent: *\nDisallow: /admin/\nHost: https://{}.ede74.ru/\nSitemap: https://{}.ede74.ru/sitemap.xml".format(subdomain,subdomain)
    else:
        robotsTxt = "User-agent: *\nDisallow: /admin/\nHost: https://ede74.ru/\nSitemap: https://ede74.ru/sitemap.xml"

    return HttpResponse(robotsTxt, content_type="text/plain")

def prices(request):
    n1 = random.randint(0, 9)
    n2 = random.randint(0, 9)
    callbackForm = CallbackForm()
    callbackOrderForm = CallbackOrderForm()
    allService = ServiceName.objects.all()
    return render(request, 'pages/prices.html', locals())

def contacts(request):
    n1 = random.randint(0, 9)
    n2 = random.randint(0, 9)
    callbackForm = CallbackForm()
    callbackOrderForm = CallbackOrderForm()
    return render(request, 'pages/contacts.html', locals())

def allPosts(request):
    allPost = BlogPost.objects.filter(is_active=True)
    return render(request, 'pages/posts.html', locals())

def showPost(request,slug):
    post = BlogPost.objects.get(name_slug=slug)
    return render(request, 'pages/post.html', locals())

def lk(request):
    n1 = random.randint(0, 9)
    n2 = random.randint(0, 9)
    subdomain = request.subdomain
    if subdomain:
        returnUrl = settings.PROTOCOL + subdomain + '.' + settings.RETURN_URL
    else:
        returnUrl = settings.PROTOCOL + settings.RETURN_URL

    print('returnUrl', returnUrl)
    if request.user.is_authenticated:
        totalFullPrice = 0
        totalActiveOrders = 0
        messageForm = MessageForm()
        orderForm = OrderForm()
        userForm = UpdateForm()
        allOrders = Order.objects.filter(user=request.user)
        for order in allOrders:
            totalFullPrice += order.fullPrice
            if order.complete and not order.is_fullPayed:
                totalActiveOrders += 1
        allService = ServiceName.objects.all()
        return render(request, 'pages/lk.html', locals())
    else:
        return render(request, 'pages/index.html', locals())




