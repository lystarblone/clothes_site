from django.db import models

# Create your models here.
"""
class User(models.Model):
    email = models.EmailField(unique=True, verbose_name='Email')
    password = models.CharField(max_length=100, verbose_name='Пароль')
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    phone = models.CharField(max_length=15, blank=True, null=True, verbose_name='Телефон')
    adress = models.TextField(blank=True, null=True, verbose_name='Адрес')

class Stuff(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название товара')
    description = models.TextField(blank=True, null=True, verbose_name='Описание товара')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    '''
    type_id = 
    collection_id = 
    img = models.ImageField()
    '''
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

class Type(models.Model):
    name = models.CharField(max_length=50, verbose_name='Тип товара')

class Collection(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название коллекции')
    description = models.TextField(blank=True, null=True, verbose_name='Описание коллекции')
"""