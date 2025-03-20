from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def main_page(request):
    return render(request, "main/index.html", {"title": "Polaris Aurora"})

def new_stuff(request):
    return HttpResponse("Новые товары")

def outerwear(request):
    return HttpResponse("Верхняя одежда")

def bottoms(request):
    return HttpResponse("Нижняя одежда")

def accessories(request):
    return HttpResponse("Аксесуары")

def sportswear(request):
    return HttpResponse("Спортивная экипировка")

def collections(request):
    return HttpResponse("Коллекции")

def guides(request):
    return render(request, "main/guides.html", {"title": "Guides"})


def page_not_found(request, exception):
    return HttpResponseNotFound('Страница не найдена')