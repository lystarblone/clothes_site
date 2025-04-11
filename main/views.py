from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator
from django.http import HttpResponseNotFound
from .models import Stuff, Collection, Type
from .forms import AuthForm

# Create your views here.

def main_page(request):
    dataset = {
        'stuffs': Stuff.objects.all(),
        "latest_stuffs": Stuff.objects.order_by('-time_create')[:10],
        "collections": Collection.objects.filter(pk__in=[4, 5]),
        'title': 'Polaris Aurora',
    }
    return render(request, "main/index.html", dataset)

def new_stuff(request):
    products = Stuff.objects.all().order_by('-pk').prefetch_related('images')
    paginator = Paginator(products, 50)

    dataset = {
        "page_obj": paginator.get_page(request.GET.get('page')),
        "title": "New Stuff"
    }
    
    return render(request, "main/new_stuff.html", dataset)

def outerwear(request):
    return render(request, "main/outerwear.html", {"title": "Outwear"})

def accessories(request):
    return render(request, "main/accessories.html", {"title": "Accessories"})

def sportswear(request):
    return render(request, "main/sportswear.html", {"title": "Sportswear"})

def collections(request):
    dataset = {
        "collections": Collection.objects.order_by('-pk').all(),
        "title": "Collections",
    }
    return render(request, "main/Collections.html", dataset)

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
            """try:
                Stuff.objects.create(**form.cleaned_data)
                return redirect("main_page")
            except:
                form.add_error(None, "ошибкаааааа!")"""
            form.save()
            return redirect("main_page")
    else:
        form = AuthForm()

    dataset = {
        "title": "Auth",
        "form": form,
    }
    return render(request, "main/auth.html", dataset)

def stuff(request, slug):
    product = get_object_or_404(Stuff, slug=slug)
    title = f"Product: {product.short_name}"
    dataset = {
        "title": title,
        "product": product,
    }
    return render(request, "main/stuff.html", dataset)

def outerwear(request):
    products = Stuff.objects.filter(type=Type.objects.get(name="Outerwear")).order_by('-pk').prefetch_related('images')
    paginator = Paginator(products, 50)

    dataset = {
        "page_obj": paginator.get_page(request.GET.get('page')),
        "title": "Outerwear"
    }
    
    return render(request, "main/outerwear.html", dataset)

def accessories(request):
    products = Stuff.objects.filter(type=Type.objects.get(name="Accessories")).order_by('-pk').prefetch_related('images')
    paginator = Paginator(products, 50)

    dataset = {
        "page_obj": paginator.get_page(request.GET.get('page')),
        "title": "Accessories"
    }
    
    return render(request, "main/accessories.html", dataset)

def sportswear(request):
    products = Stuff.objects.filter(type=Type.objects.get(name="Sportswear")).order_by('-pk').prefetch_related('images')
    paginator = Paginator(products, 50)

    dataset = {
        "page_obj": paginator.get_page(request.GET.get('page')),
        "title": "Sportswear"
    }
    
    return render(request, "main/sportswear.html", dataset)

def page_not_found(request, exception):
    return HttpResponseNotFound('Страница не найдена')