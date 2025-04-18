from django.urls import include, path
from . import views

urlpatterns = [
    path("cart/", views.cart, name="cart"),
]