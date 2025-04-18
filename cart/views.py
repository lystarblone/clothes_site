from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def cart(request):
    dataset = {
        "title": "Cart"
    }
    return render(request, "cart/cart.html", dataset)