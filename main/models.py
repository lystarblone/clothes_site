from django.db import models

# Create your models here.

class User(models.Model):
    email = models.EmailField(unique=True, verbose_name='Email')
    password = models.CharField(max_length=100, verbose_name='Password')
    first_name = models.CharField(max_length=50, verbose_name='Name')
    last_name = models.CharField(max_length=50, verbose_name='Surname')
    phone = models.CharField(max_length=15, blank=True, null=True, verbose_name='Phone number')
    adress = models.TextField(blank=True, null=True, verbose_name='Adress')

class Type(models.Model):
    name = models.CharField(max_length=50, verbose_name='Stuff type')

    def __str__(self):
        return self.name

class Collection(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Collection name')
    description = models.TextField(blank=True, null=True, verbose_name='Collection description')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='Slug')
    image = models.ImageField(null=True, verbose_name="Image")

    def __str__(self):
        return self.name

class Stuff(models.Model):
    name = models.CharField(max_length=50, unique=True, db_index=True, verbose_name='Stuff name')
    short_name = models.CharField(max_length=50, blank=True, verbose_name='Short stuff name')
    description = models.TextField(blank=True, null=True, verbose_name='Stuff description')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='Slug')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price')
    
    type = models.ForeignKey(
        Type,
        on_delete=models.CASCADE,
        related_name='stuff_items',
        verbose_name='Stuff type',
        default=1
    )
    
    collection = models.ForeignKey(
        Collection,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='stuff_items',
        verbose_name='Collection'
    )

    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Created')

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