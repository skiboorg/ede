from django.urls import path
from . import views
from django.views.generic.base import RedirectView


urlpatterns = [
    path('', views.index, name='index'),
    path('robots.txt', views.robots, name='robots'),
    path('index.html', RedirectView.as_view(url='/', permanent=False), name='index'),
    path('index.php', RedirectView.as_view(url='/', permanent=False), name='index'),
    path('prices/', views.prices, name='prices'),
    path('contacts/', views.contacts, name='contacts'),
    path('lk/', views.lk, name='lk'),
    path('posts/', views.allPosts, name='allposts'),
    path('post/<slug>/', views.showPost, name='showpost'),


]