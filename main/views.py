from django.shortcuts import render
from django.http import HttpResponseNotFound
from .models import Stuff

# Create your views here.

def main_page(request):
    return render(request, "main/index.html", {"title": "Polaris Aurora"})

def new_stuff(request):
    return render(request, "main/new_stuff.html", {"title": "New Stuff"})

def all_stuff(request):
    stuffs = Stuff.objects.all()
    dataset = {
        'stuffs': stuffs,
        'title': 'All Stuff',
    }
    return render(request, "main/all_stuff.html", dataset)

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
    return render(request, "main/client_resources/main.html", {"title": "Client Resources"})

def delivery(request):
    return render(request, "main/client_resources/delivery.html", {"title": "Delivery"})

def pickup(request):
    return render(request, "main/client_resources/pickup.html", {"title": "Pickup"})

def payment(request):
    return render(request, "main/client_resources/payment.html", {"title": "Payment"})

def returns_and_refunds(request):
    return render(request, "main/client_resources/returns_and_refunds.html", {"title": "Returns and refunds"})

def size_guide(request):
    return render(request, "main/client_resources/size_guide.html", {"title": "Size Guide"})

def contacts(request):
    return render(request, "main/client_resources/contacts.html", {"title": "Contacts"})

def privacy_policy(request):
    return render(request, "main/client_resources/privacy_policy.html", {"title": "Privacy Policy"})

def terms_of_use(request):
    return render(request, "main/client_resources/terms_of_use.html", {"title": "Terms of Use"})

def page_not_found(request, exception):
    return HttpResponseNotFound('Страница не найдена')