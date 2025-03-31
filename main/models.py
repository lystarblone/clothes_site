from django.db import models

# Create your models here.

class User(models.Model):
    email = models.EmailField(unique=True, verbose_name='Email')
    password = models.CharField(max_length=100, verbose_name='Пароль')
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    phone = models.CharField(max_length=15, blank=True, null=True, verbose_name='Телефон')
    adress = models.TextField(blank=True, null=True, verbose_name='Адрес')

class Type(models.Model):
    name = models.CharField(max_length=50, verbose_name='Тип товара')

    def __str__(self):
        return self.name

class Collection(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название коллекции')
    description = models.TextField(blank=True, null=True, verbose_name='Описание коллекции')

    def __str__(self):
        return self.name

class Stuff(models.Model):
    name = models.CharField(max_length=50, unique=True, db_index=True, verbose_name='Название товара')
    description = models.TextField(blank=True, null=True, verbose_name='Описание товара')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='Слаг')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    
    type = models.ForeignKey(
        Type,
        on_delete=models.CASCADE,
        related_name='stuff_items',
        verbose_name='Тип товара',
        default=1
    )
    
    collection = models.ForeignKey(
        Collection,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='stuff_items',
        verbose_name='Коллекция'
    )

    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.name
    
class StuffImage(models.Model):
    stuff = models.ForeignKey(
        Stuff,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name='Товар'
    )

    image = models.ImageField(upload_to='stuff_images/', verbose_name='Изображение')