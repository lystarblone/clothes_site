from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart, name='cart'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/update/<int:item_id>/', views.update_cart, name='update_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('checkout/gift_cards/', views.gift_card_payment, name='gift_card_payment'),
    path('checkout/cryptocurrency/', views.cryptocurrency_payment, name='cryptocurrency_payment'),
    path('checkout/payment_confirmation/', views.payment_confirmation, name='payment_confirmation'),
]