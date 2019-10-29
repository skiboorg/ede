from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('prices/', views.prices, name='prices'),
    path('contacts/', views.contacts, name='contacts'),
    path('lk/', views.lk, name='lk'),
    path('posts/', views.allPosts, name='allposts'),
    path('post/<slug>', views.showPost, name='showpost'),


]