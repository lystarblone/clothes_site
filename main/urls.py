from django.urls import path
from . import views

urlpatterns = [
    path("", views.main_page, name="main_page"),
    path("new_stuff/", views.new_stuff, name="new_stuff"),
    path("outerwear/", views.outerwear, name="outerwear"),
    path("bottoms/", views.bottoms, name="bottoms"),
    path("accessories/", views.accessories, name="accessories"),
    path("sportswear/", views.sportswear, name="sportswear"),
    path("collections/", views.collections, name="collections"),
    path("client_resources/", views.guides, name="guides"),
]