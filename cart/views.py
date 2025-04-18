from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from main.models import Stuff
from .models import CartItem
from django.views.decorators.http import require_POST

@login_required(login_url='users:login')
def cart(request):
    cart_items = CartItem.objects.filter(user=request.user).order_by('-id')
    total_price = sum(item.product.price * item.quantity for item in cart_items)

    dataset = {
        'cart_items': cart_items,
        'total_price': total_price,
        'title': 'Cart'
    }
    return render(request, 'cart/cart.html', dataset)

@login_required(login_url='users:login')
def add_to_cart(request, product_id):
    if request.method == 'POST':
        size = request.POST.get('size')  # Получаем выбранный размер из формы
        quantity = int(request.POST.get('quantity', 1))  # Получаем количество (по умолчанию 1)

        product = get_object_or_404(Stuff, id=product_id)

        # Проверяем, есть ли уже такой товар с таким размером в корзине
        cart_item, created = CartItem.objects.get_or_create(
            user=request.user,
            product=product,
            size=size,
            defaults={'quantity': quantity}
        )

        if not created:
            cart_item.quantity += quantity
            cart_item.save()

    return redirect('product_detail', slug=product.slug)

@require_POST
def update_cart(request, item_id):
    # Находим элемент корзины по ID
    cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
    action = request.POST.get('action')

    if action == 'increase':
        # Увеличиваем количество
        cart_item.quantity += 1
        cart_item.save()
    elif action == 'decrease':
        if cart_item.quantity > 1:
            # Уменьшаем количество
            cart_item.quantity -= 1
            cart_item.save()
        else:
            # Удаляем элемент из корзины, если количество меньше 1
            cart_item.delete()

    # Перенаправляем на страницу корзины
    return redirect('cart:cart')