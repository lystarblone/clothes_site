from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from main.models import Stuff
from .models import CartItem
from django.views.decorators.http import require_POST
from django.contrib import messages
from decimal import Decimal


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

def product_detail(request, product_id):
    product = get_object_or_404(Stuff, id=product_id)
    selected_size = None
    in_cart = False

    if request.method == 'POST':
        # Получаем выбранный размер из POST-запроса
        selected_size = request.POST.get('size', None)
        if 'add_to_cart' in request.POST:
            if selected_size:
                # Логика добавления товара в корзину
                cart_item, created = CartItem.objects.get_or_create(
                    user=request.user,
                    product=product,
                    size=selected_size,
                    defaults={'quantity': 1}
                )
                if not created:
                    cart_item.quantity += 1
                    cart_item.save()
                messages.success(request, f"Product '{product.name}' added to cart with size {selected_size}.")
                in_cart = True
            else:
                messages.error(request, "Please select a size before adding to cart.")

    # Если товар уже в корзине, проверяем его состояние
    cart_item = CartItem.objects.filter(product=product, user=request.user).first()
    if cart_item:
        in_cart = True
        selected_size = cart_item.size  # Устанавливаем размер из корзины

    return render(request, 'product_detail.html', {
        'product': product,
        'selected_size': selected_size,  # Передаем выбранный размер в шаблон
        'in_cart': in_cart,  # Передаем состояние корзины в шаблон
    })


# cart/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CartItem

@login_required(login_url='users:login')
def checkout(request):
    if request.method == 'POST':
        # Получаем данные из формы
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        country = request.POST.get('country')
        city = request.POST.get('city')
        address = request.POST.get('address')
        payment_method = request.POST.get('payment_method')

        # Проверяем, заполнены ли обязательные поля
        if not all([first_name, last_name, email, country, city, address]):
            messages.error(request, "Please fill in all required fields.")
            return redirect('cart:checkout')

        # Проверяем, выбран ли метод оплаты
        if not payment_method:
            messages.error(request, "Please select a payment method.")
            return redirect('cart:checkout')

        # Переадресация на соответствующую страницу оплаты
        if payment_method == 'gift_cards':
            return redirect('cart:gift_card_payment')  # Страница оплаты сертификатами
        elif payment_method == 'cryptocurrency':
            return redirect('cart:cryptocurrency_payment')  # Страница оплаты криптовалютой

    # Если метод GET, отображаем страницу оформления заказа
    cart_items = CartItem.objects.filter(user=request.user).order_by('-id')
    total_price = sum(item.product.price * item.quantity for item in cart_items)

    context = {
        'cart_items': cart_items,
        'total_price': total_price,
        'user': request.user,
    }

    return render(request, 'cart/checkout.html', context)

@login_required(login_url='users:login')
def gift_card_payment(request):
    error_message = None  # Переменная для хранения ошибки

    if request.method == 'POST':
        # Получаем введенный код сертификата
        gift_card_code = request.POST.get('gift_card_code')

        # Проверяем, что код состоит из 16 символов
        if not gift_card_code or len(gift_card_code) != 16:
            error_message = "Invalid gift card code. Please enter a 16-digit code."
            return render(request, 'cart/gift_card_payment.html', {'error_message': error_message})

        # Пример проверки (замените на реальную логику)
        if gift_card_code != "VALIDCODE12345678":
            error_message = "A gift card with this code does not exist."
            return render(request, 'cart/gift_card_payment.html', {'error_message': error_message})

        # Если код верный, переадресуем на страницу подтверждения заказа
        return redirect('cart:order_confirmation')

    # Если метод GET, просто отображаем страницу
    return render(request, 'cart/gift_card_payment.html', {'error_message': error_message})

@login_required(login_url='users:login')
def cryptocurrency_payment(request):
    # Получаем все товары из корзины текущего пользователя
    cart_items = CartItem.objects.filter(user=request.user).order_by('-id')

    # Рассчитываем общую стоимость заказа (total_price)
    total_price = sum(item.product.price * item.quantity for item in cart_items)

    # Преобразуем коэффициент 1.2 в Decimal
    eth_coefficient = Decimal('1.293475457893678')

    # Рассчитываем сумму в ETH (умножаем на коэффициент 1.2)
    total_price_in_eth = round(total_price * eth_coefficient, 8)

    if request.method == 'POST':
        # Очищаем корзину пользователя
        cart_items.delete()

        # Переадресуем на страницу подтверждения платежа
        return redirect('cart:payment_confirmation')

    context = {
        'total_price_in_eth': total_price_in_eth,
    }

    return render(request, 'cart/cryptocurrency_payment.html', context)


@login_required(login_url='users:login')
def payment_confirmation(request):
    return render(request, 'cart/payment_confirmation.html')