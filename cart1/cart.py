import datetime
from magaz.models import Prises
from django.conf import settings


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = request.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __len__(self):

        return sum(item['quantity'] for item in self.cart.values())

    def __iter__(self):
        goods_ids = self.cart.keys()
        prises = Prises.objects.filter(id__in=goods_ids)
        for prise in prises:
            self.cart[str(prise.id)]['prise'] = prise

        for item in self.cart.values():
            item['good_price'] = (item['good_price'])
            item['total_good_price'] = item['good_price'] * item['quantity']
            yield item

    def add(self, prise, quantity=1,  update_quantity=False):
        good_id = str(prise.id)
        if good_id not in self.cart:
            self.cart[good_id] = {'quantity': 0,
                                  'good_price': str(prise.good_price)}

        if update_quantity:
            self.cart[good_id]['quantity'] = quantity
        else:
            self.cart[good_id]['quantity'] += quantity
        self.save()

    def remove(self, prise):
        prise_id = str(prise.id)
        if prise_id in self.cart:
            del self.cart[prise_id]
            self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def clear(self):
        self.session[settings.CART_SESSION_ID] = {}
        self.session.modified = True

    def get_total_price(self):
        return sum(int(item['good_price']) * item['quantity'] for item in self.cart.values())