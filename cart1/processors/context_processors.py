from cart1.cart import Cart


def cart(request):
    return {'cart': Cart(request)}