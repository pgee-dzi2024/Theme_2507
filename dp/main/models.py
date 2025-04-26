from django.db import models
from datetime import date


# Create your models here.
class Article(models.Model):
    title = models.CharField('Заглавие', max_length=200)
    content = models.TextField('Съдържание')
    author = models.CharField('Автор', max_length=50)
    published = models.DateField('Публикувано на', default=date.today)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статия'
        verbose_name_plural = 'Статии'


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    text = models.TextField('Коментар')
    author = models.CharField('Автор', max_length=50)

    def __str__(self):
        return self.author

    class Meta:
        verbose_name = 'Коментар'
        verbose_name_plural = 'Коментари'
