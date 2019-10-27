from django.urls import path
from . import views

urlpatterns = [
   path('workprice/', views.createCallbackForm, name='createCallbackForm'),
   path('callback/', views.createCallbackOrderForm, name='createCallbackOrderForm'),


]
