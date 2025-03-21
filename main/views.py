from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def main_page(request):
    return render(request, "main/index.html", {"title": "Polaris Aurora"})

def new_stuff(request):
    return render(request, "main/new_stuff.html", {"title": "New Stuff"})

def outerwear(request):
    return render(request, "main/outerwear.html", {"title": "Outwear"})

def bottoms(request):
    return render(request, "main/bottoms.html", {"title": "Bottoms"})

def accessories(request):
    return render(request, "main/accessories.html", {"title": "Accessories"})

def sportswear(request):
    return render(request, "main/sportswear.html", {"title": "Sportswear"})

def collections(request):
    return render(request, "main/Collections.html", {"title": "Collections"})

def guides(request):
    return render(request, "main/guides.html", {"title": "Guides"})


def page_not_found(request, exception):
    return HttpResponseNotFound('Страница не найдена')