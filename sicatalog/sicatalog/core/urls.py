from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('categories/', categories, name='categories'),
    path('products/', products, name='products'),
    path('login/', login,  name='login'),
    path('signup/', register,  name='signup'),
    path('account/', account, name='account'),
    path('about/', about, name='about'),
    path('subscribe/', subscribe, name='subscribe'),
]