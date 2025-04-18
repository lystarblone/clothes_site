from django.db import models
from django.conf import settings
from main.models import Stuff

# Create your models here.
from django.conf import settings

class CartItem(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='cart_items',
        verbose_name='User'
    )
    product = models.ForeignKey(
        Stuff,  # Связь с товаром
        on_delete=models.CASCADE,
        related_name='cart_items',
        verbose_name='Stuff'
    )
    size = models.CharField(max_length=10, verbose_name='Size')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Count')

    def __str__(self):
        return f"{self.product.name} ({self.size}) - {self.quantity}"