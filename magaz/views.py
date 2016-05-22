from django.shortcuts import render, get_object_or_404
from magaz.models import Prises, Category
from cart1.forms import CartAddProductsForm



def shop(request):
    categories = Category.objects.order_by('-cat_name')
    goods = Prises.objects.order_by('-good_time')
    context = {'categories': categories,
               'goods': goods,
                }
    return render(request, 'magaz/shop1.html', context)      #длля продолжения работы с категориями заменить на шоп1


def cat_detail(request, slag_url):
    category = get_object_or_404(Category, slag_url=slag_url)
    goods = Prises.objects.order_by('-good_time')

    return render(request, 'magaz/cat_detail.html', {'category': category, 'goods': goods})



def show_goods(request, good_id):
    prices = get_object_or_404(Prises, id=good_id)
    cart_product_form = CartAddProductsForm()
    return render(request, 'magaz/good.html', {'prices': prices, 'cart_product_form': cart_product_form})
