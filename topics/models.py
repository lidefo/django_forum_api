from django.contrib.auth import get_user_model
from pytils.translit import slugify
from django.db import models

# Create your models here.
User = get_user_model()

class Topic(models.Model):
    '''Topic contains messages.'''
    title = models.CharField(max_length=50, null=False,verbose_name='Название', unique=True)
    description = models.TextField(max_length=3500, null=False,verbose_name='Описание')
    create_date = models.DateTimeField(auto_now=True, verbose_name='Дата создания')
    author = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Создатель темы')
    slug = models.SlugField(default='', null=False)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Topic, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Message(models.Model):
    '''Message model.'''
    text = models.TextField(max_length=3500, verbose_name='Текст')
    create_date = models.DateTimeField(auto_now=True, verbose_name='Дата публикации')
    author = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Создатель публикации')
    topic = models.ForeignKey(Topic, default='', on_delete=models.CASCADE, verbose_name='Тред сообщения')

    def __str__(self):
        return str(self.author) + ' | ' + str(self.create_date)
