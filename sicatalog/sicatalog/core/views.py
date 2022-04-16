from django.http import HttpResponse
from django.shortcuts import render, redirect

menu = [{'title': "Категории", 'url_name': 'categories'},
        {'title': "Товары", 'url_name': 'products'},
        {'title': "Подбор Автомобилей", 'url_name': 'subscribe'},
        {'title': "Регистрация", 'url_name': 'signup'},
        {'title': "О нас", 'url_name': 'about'},
        {'title': "Логин", 'url_name': 'login'}
        ]


def index(request):
    context = {
        'menu': menu,
        'title': 'Si-Home'
    }
    return render(request, 'core/index.html', context=context)


def categories(request):
    return render(request, 'core/categories.html')


def products(request):
    return render(request, 'core/products.html')


def login(request):
    return render(request, 'core/login.html')


def register(request):
    return render(request, 'core/register.html')


def account(request):
    return render(request, 'core/account.html')


def about(request):
    return render(request, 'core/about.html')


def subscribe(request):
    return render(request, 'core/subscribe.html')