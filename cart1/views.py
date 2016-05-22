from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .cart import Cart
from magaz.models import Prises
from .forms import CartAddProductsForm


@require_POST
def cart_add(request, good_id):
    cart = Cart(request)
    price = get_object_or_404(Prises, id=good_id)
    form = CartAddProductsForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(prise=price,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart1:cart_detail')

def cart_remove(request, good_id):
    cart = Cart(request)
    price = get_object_or_404(Prises, id=good_id)
    cart.remove(price)
    return redirect('cart1:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductsForm(initial={'quantity': item['quantity'],
                                                                    'update': True})
    return render(request, 'cart/detail.html', {'cart': cart})