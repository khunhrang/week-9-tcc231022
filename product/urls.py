#product/urls.py

from django.urls import path
from .views import Home, About, Mobile

urlpatterns = [
    path('', Home,name='home-page'),
    path('about/', About,name='about-page'),
    path('mobile/', Mobile, name='mobile-page'),
]