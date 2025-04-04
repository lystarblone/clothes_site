from django.shortcuts import redirect, render
from django.http import HttpResponseNotFound
from .models import Stuff
from .forms import AuthForm

# Create your views here.

def main_page(request):
    dataset = {
        'stuffs': Stuff.objects.all(),
        "latest_stuffs": Stuff.objects.order_by('-time_create')[:10],
        'title': 'Polaris Aurora',
    }
    return render(request, "main/index.html", dataset)

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

def auth(request):
    if request.method == "POST":
        form = AuthForm(request.POST)
        if form.is_valid():
            try:
                Stuff.objects.create(**form.cleaned_data)
                return redirect("main_page")
            except:
                form.add_error(None, "ошибкаааааа!")
    else:
        form = AuthForm()

    dataset = {
        "title": "Terms of Use",
        "form": form,
    }
    return render(request, "main/auth.html", dataset)

def page_not_found(request, exception):
    return HttpResponseNotFound('Страница не найдена')