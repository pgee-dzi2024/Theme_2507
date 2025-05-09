from django.shortcuts import render
from .models import Article, Comment
from django.http import HttpResponseRedirect
from django.urls import reverse


def index(request):
    articles = Article.objects.order_by('-id')[:2]
    params = {'page_title': 'ГЛАВНА СТРАНИЦА',
              'page_header': 'Главна страница',
              'page_content': 'Текст на страницата',
              'articles': articles,
              }
    return render(request, 'main/index.html', params)


def all_articles(request):
    articles = Article.objects.order_by('-id')
    params = {'page_title': 'Всички публикации',
              'page_header': 'Всички публикации',
              'page_content': 'Пълен списък на всички публикации',
              'articles': articles,
              }

    return render(request, 'main/index.html', params)


def single_article(request, article_id):
    article = Article.objects.get(id=article_id)
    comments = article.comment_set.order_by('-id')
    params = {'page_title': 'публикация №'+str(article_id),
              'article': article,
              'comments': comments,
              }
    return render(request, 'main/article.html', params)


def form_action(request, article_id):
    article = Article.objects.get(id=article_id)
    print(request.POST)
    article.comment_set.create(author=request.POST['name'], text=request.POST['message'])
    return HttpResponseRedirect(reverse('single', args=(article.id, )))
