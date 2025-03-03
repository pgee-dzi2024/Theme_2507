from django.db import models
from datetime import date

from django.utils import timezone


# Модел за статиите в блога
class Article(models.Model):
    title = models.CharField('Заглавие', max_length=200)
    content = models.TextField('Съдържание')
    picture = models.ImageField('Снимка', upload_to='images', blank=True)
    author = models.CharField('Автор', max_length=50)
    published = models.DateField('Публикувано на', default=date.today)

    def __str__(self):
        return f'{self.title} от {self.author}'

    class Meta:
        verbose_name = 'Статия'
        verbose_name_plural = 'Статии'


# Модел за съобщения от формата за контакти
class Message(models.Model):
    name = models.CharField('име', max_length=200, default='', blank=True)
    email = models.EmailField('e-mail', max_length=200, blank=True)
    phone = models.CharField('телефон', max_length=200, blank=True)
    message = models.TextField('съобщение')
    published = models.DateField('Дата/час на получаване', default=timezone.now)

    def __str__(self):
        return f'Съобщение от {self.name}'

    class Meta:
        verbose_name = 'Съобщение'
        verbose_name_plural = 'Съобщения'
