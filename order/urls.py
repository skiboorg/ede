from django.urls import path
from . import views

urlpatterns = [
   path('new/', views.newOrder, name='newOrder'),
   path('message/', views.newMesage, name='newMesage'),
   path('pay/', views.pay, name='pay'),
   path('pay_complete/', views.pay_complete, name='pay_complete'),




]
