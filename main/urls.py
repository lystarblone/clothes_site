from django.urls import path
from . import views

urlpatterns = [
    path("", views.main_page, name="main_page"),
    path("new_stuff/", views.new_stuff, name="new_stuff"),
    path("all_stuff/", views.all_stuff, name="all_stuff"),
    path("outerwear/", views.outerwear, name="outerwear"),
    path("bottoms/", views.bottoms, name="bottoms"),
    path("accessories/", views.accessories, name="accessories"),
    path("sportswear/", views.sportswear, name="sportswear"),
    path("collections/", views.collections, name="collections"),
    path("client_resources/main", views.guides, name="client_resources"),
    path("client_resources/delivery", views.delivery, name="delivery"),
    path("client_resources/pickup", views.pickup, name="pickup"),
    path("client_resources/payment", views.payment, name="payment"),
    path("client_resources/returns_and_refunds", views.returns_and_refunds, name="returns_and_refunds"),
    path("client_resources/size_guide", views.size_guide, name="size_guide"),
    path("client_resources/contacts", views.contacts, name="contacts"),
    path("client_resources/privacy_policy", views.privacy_policy, name="privacy_policy"),
    path("client_resources/terms_of_use", views.terms_of_use, name="terms_of_use"),
]