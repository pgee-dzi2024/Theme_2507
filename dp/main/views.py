from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def index0(request):
    return HttpResponse('<h4> Главна страница </h4>')


def index1(request):
    params = {'title': 'ГЛАВНА СТРАНИЦА',
              'body': 'Текст на страницата',
              }
    return render(request, 'main/base_template.html', params)


def index(request):
    articles = Article.objects.all()
    params = {'articles': articles, }
    return render(request, 'main/index.html', params)


def contact(request):
    return render(request, 'main/contact.html')


def about(request):
    return render(request, 'main/about.html')


def post(request, art_id):
    article = Article.objects.get(id=art_id)

    return render(request, 'main/post.html', {'article': article, })
