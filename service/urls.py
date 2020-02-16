from django.urls import path
from . import views
from django.views.generic.base import RedirectView


urlpatterns = [
    path('', views.index, name='index'),
    path('robots.txt', views.robots, name='robots'),
    path('index.html', RedirectView.as_view(url='/', permanent=False), name='index1'),
    path('index.php', RedirectView.as_view(url='/', permanent=False), name='index2'),
    path('services/', views.services, name='services'),
    path('services/<name_slug>/', views.service, name='service'),
    path('services/<name_slug>/<subservice>', views.subservice, name='subservice'),
    path('contacts/', views.contacts, name='contacts'),
    path('lk/', views.lk, name='lk'),
    path('posts/', views.allPosts, name='allposts'),
    path('policy/', views.policy, name='policy'),
    path('posts/<slug>/', views.showPost, name='showpost'),


]