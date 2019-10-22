from django.urls import path
from . import views

urlpatterns = [
   path('create/', views.createCallbackForm, name='createCallbackForm'),


]
