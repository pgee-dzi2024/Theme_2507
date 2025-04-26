from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='latest'),
    path('all_articles', views.all_articles, name='all'),
    path('<int:article_id>/', views.single_article, name='single'),
    path('<int:article_id>/form_action', views.form_action, name='form_action'),

]
