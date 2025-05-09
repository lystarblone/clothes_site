from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, verbose_name='Email')
    first_name = models.CharField(max_length=50, verbose_name='Name')
    last_name = models.CharField(max_length=50, verbose_name='Surname')
    phone = models.CharField(max_length=15, blank=True, null=True, verbose_name='Phone number')
    address = models.TextField(blank=True, null=True, verbose_name='Address')
    postal_code = models.CharField(max_length=20, blank=True, null=True, verbose_name='Postal Code')

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

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