from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from magaz.forms import *
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
    cabinet = 'cabinet'
    sif = SiteMiniForm(request.POST)
    skf = SkypeMiniForm(request.POST)
    prf = ProfessionMiniForm(request.POST)
    nmf = NumbMiniForm(request.POST)
    abf = AboutMiniForm(request.POST)
    avf = AvatarMiniForm(request.POST)
    return render(request, 'magaz/cabinet.html', {'cabinet': cabinet, 'sif': sif, 'skf': skf, 'prf': prf, 'nmf': nmf,
                                                  'abf': abf, 'avf': avf})


def siteform(request):
    user = request.user
    if request.method == 'POST':
        site_form = SiteMiniForm(request.POST)
        if site_form.is_valid():
            sitesave = site_form.save(commit=False)
            sitesave.user = user
            sitesave.save()
            return HttpResponseRedirect('/shop/cabinet')
    else:
        site_obj = SiteUser.objects.get(user=request.user)
        site_form = SkypeMiniForm(instance= site_obj)
        return render(request, 'magaz/forms/site.html', {'site_form': site_form})


def skypeform(request):
    user = request.user
    if request.method == 'POST':
        skype_form = SkypeMiniForm(request.POST)
        if skype_form.is_valid():
            skypesave = skype_form.save(commit=False)
            skypesave.user = user
            skypesave.save()
            return HttpResponseRedirect('/shop/cabinet')
    else:
        skype_obj = SkypeUser.objects.get(user=request.user)
        skype_form = SkypeMiniForm(instance= skype_obj)
        return render(request, 'magaz/forms/skype.html', {'skype_form': skype_form})


def professionform(request):
    user = request.user
    if request.method == 'POST':
        profession_form = ProfessionMiniForm(request.POST)
        if profession_form.is_valid():
            professionsave = profession_form.save(commit=False)
            professionsave.user = user
            professionsave.save()
            return HttpResponseRedirect('/shop/cabinet')
    else:
        # pro_obj = ProfessionalUser.objects.get(user=request.user)
        profession_form = ProfessionMiniForm()
        return render(request, 'magaz/forms/profess.html', {'profession_form': profession_form})


def numbform(request):
    user = request.user
    if request.method == 'POST':
        numb_form = NumbMiniForm(request.POST)
        if numb_form.is_valid():
            numbsave = numb_form.save(commit=False)
            numbsave.user = user
            numbsave.save()
            return HttpResponseRedirect('/shop/cabinet')
    else:
        numb_form = NumbMiniForm()
        return render(request, 'magaz/forms/numb.html', {'numb_form': numb_form})


def aboutform(request):
    user = request.user
    if request.method == 'POST':
        about_form = AboutMiniForm(request.POST)
        if about_form.is_valid():
            aboutsave = about_form.save(commit=False)
            aboutsave.user = user
            aboutsave.save()
            return HttpResponseRedirect('/shop/cabinet')
    else:
        about_form = AboutMiniForm()
        return render(request, 'magaz/forms/about.html', {'about_form': about_form})

def avatarform(request):
    user = request.user
    if request.method == 'POST':
        avatar_form = AvatarMiniForm(request.POST)
        if avatar_form.is_valid():
            avatarsave = avatar_form.save(commit=False)
            avatarsave.user = user
            if 'avatar' in request.FILES:
                avatarsave.avatar = request.FILES['avatar']
            avatarsave.save()
            return HttpResponseRedirect('/shop/cabinet')
    else:
        avatar_form = AvatarMiniForm()
    return render(request, 'magaz/forms/avatar.html', {'avatar_form': avatar_form})


def just_pay_for_all(request):
    cart = Cart(request)
    user = request.user
    if request.method == 'POST':
        form = PayGoodForm(request.POST)
        if form.is_valid():
            for item in cart:
                GoodPay.objects.create(
                    user=user,
                    prises=item['prise']
                )
            return render(request, {cart: 'cart', form: 'form'})
        else:
            form = PayGoodForm()

"""
    if request.method == 'POST':
        cabinet_form = CabinetForm(request.POST)
        user = User.objects.get(pk=request.user.id)

        if cabinet_form.is_valid():
            profile = cabinet_form.save(commit=False)
            profile.user = user

            if 'avatar' in request.FILES:
                profile.avatar = request.FILES['avatar']
            profile.save()
        else:
            print(cabinet_form.errors)
    else:
        cabinet_form = CabinetForm()
"""


