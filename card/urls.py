from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('news/', views.news, name='news'),
    path('locations/', views.locations, name='locations'),
    path('reviews/', views.reviews, name='reviews'),
]