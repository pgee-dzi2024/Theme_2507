from django.shortcuts import render
from django.http import HttpResponse


def index0(request):
    return HttpResponse('<h4> Главна страница </h4>')


def index1(request):
    params = {'title': 'ГЛАВНА СТРАНИЦА',
              'body': 'Текст на страницата',
              }
    return render(request, 'main/base_template.html', params)


def index(request):
    return render(request, 'main/index.html')


def contact(request):
    return render(request, 'main/contact.html')


def about(request):
    return render(request, 'main/about.html')


def post(request):
    return render(request, 'main/post.html')
