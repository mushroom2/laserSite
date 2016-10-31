from cart1.cart import Cart
from magaz.userdata import UserData
from magaz.forms import *
from django.shortcuts import HttpResponseRedirect



def cart(request):
    return {'cart': Cart(request)}

def valute(request):
    hrivra_form = HrivnaForm(request.POST)
    vf = ValuteForm(request.POST)
    val = Prises.valute
    return {'vf': vf, 'hrivra_form': hrivra_form, 'val': val}