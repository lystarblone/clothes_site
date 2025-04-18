from django.db import models
from django.conf import settings
from main.models import Stuff

# Create your models here.
class CartItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Stuff, on_delete=models.CASCADE)
    size = models.CharField(max_length=10)  # Размер товара
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} ({self.size}) - {self.quantity}"