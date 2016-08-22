from django.shortcuts import render, get_object_or_404
from magaz.forms import CabinetForm
from magaz.models import Prises, Category
from cart1.forms import CartAddProductsForm
from cart1.cart import Cart
from django.contrib.auth.models import User



def shop(request):
    categories = Category.objects.order_by('-cat_name')
    goods = Prises.objects.order_by('-good_time')
    cart= Cart(request)
    context = {'categories': categories,
               'goods': goods,
               'cart': cart}
    return render(request, 'magaz/shop1.html', context)      #длля продолжения работы с категориями заменить на шоп1


def cat_detail(request, slag_url):
    category = get_object_or_404(Category, slag_url=slag_url)
    goods = Prises.objects.order_by('-good_time')
    cart= Cart(request)

    return render(request, 'magaz/cat_detail.html', {'category': category, 'goods': goods, 'cart': cart})



def show_goods(request, good_id):
    prices = get_object_or_404(Prises, id=good_id)
    cart_product_form = CartAddProductsForm()
    cart= Cart(request)
    return render(request, 'magaz/good.html', {'prices': prices, 'cart_product_form': cart_product_form, 'cart': cart})


def cabinet(request):
    if request.method == 'POST':
        cabinet_form = CabinetForm(request.POST)
        user = User
        user = request.user

        if cabinet_form.is_valid():
            profile = cabinet_form.save(commit=False)
            profile.user = user

            if 'avatar' is request.FILES:
                profile.avatar = request.FILES['avatar']
            profile.save()
        else:
            print(cabinet_form.errors)
    else:
        cabinet_form = CabinetForm()
    return render(request, 'magaz/cabinet.html', {'cabinet_form': cabinet_form})

