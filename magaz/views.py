from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from magaz.forms import *
from magaz.models import Prises, Category, GoodPay
from cart1.forms import CartAddProductsForm
from cart1.cart import Cart
from magaz.userdata import UserData
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
    return render(request, 'magaz/cat_detail.html', {'category': category, 'goods': goods, })



def show_goods(request, good_id):
    prices = get_object_or_404(Prises, id=good_id)
    cart_product_form = CartAddProductsForm()
    cart= Cart(request)
    return render(request, 'magaz/good.html', {'prices': prices, 'cart_product_form': cart_product_form, 'cart': cart})


def cabinet(request):
    cabinet = 'cabinet'
    userpay = GoodPay.objects.filter(user=request.user).order_by('-date').values()
    pr = Prises.objects.all().values('id', 'good_name')
    sif = SiteMiniForm(request.POST)
    skf = SkypeMiniForm(request.POST)
    prf = ProfessionMiniForm(request.POST)
    nmf = NumbMiniForm(request.POST)
    abf = AboutMiniForm(request.POST)
    avf = AvatarMiniForm(request.POST)
    return render(request, 'magaz/cabinet.html', {'cabinet': cabinet, 'sif': sif, 'skf': skf, 'prf': prf, 'nmf': nmf,
                                                  'abf': abf, 'avf': avf, 'userpay': userpay, 'pr': pr})


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
    order = 'order'
    user = request.user
    cart = Cart(request)
    if request.method == 'POST':
        form = PayGoodForm(request.POST)
        if form.is_valid():
            formsave = form.save(commit=False)
            formsave.user =user
            for item in cart:
                GoodPay.objects.create(
                    user=user,
                    prises=item['prise'],
                    price=item['good_price'],
                    quantity=item['quantity'],
                    ordersum=int(item['good_price'])*item['quantity']
                )
            cart.clear()
            return HttpResponseRedirect('/')

    else:
        form = PayGoodForm()

    return render(request, 'magaz/order.html', {order: 'order', cart: 'cart', form: 'form'})  #


def set_uah(request):
    val = UserData(request)
    val.setuah()
    return HttpResponseRedirect(request.GET.get('next'))


def set_usd(request):
    val = UserData(request)
    val.setdolar()
    return HttpResponseRedirect(request.GET.get('next'))

def orderformr(request):
    cart = Cart(request)
    if request.method == 'POST':
        orderform = OrderForm(request.POST)

        if orderform.is_valid():
            username = orderform.cleaned_data['clientname'] + ' from ' + str(orderform.cleaned_data['clientmail'])
            sender = orderform.cleaned_data['clientmail']
            message = 'клієнт: ' + str(orderform.cleaned_data['clientname']) + ';' + str(orderform.cleaned_data['clientsnumb']) + str(orderform.cleaned_data['clientdevelop']) + 'замовлення: ' + str(cart.cart)




            recipients = ['avi.upsale@gmail.com']

            try:
                send_mail(username, message, sender, recipients)
            except BadHeaderError:
                return HttpResponse('something goes wrong ;(')
            return HttpResponseRedirect('/thanks')

    else:
        orderform = OrderForm()
    return render(request, 'magaz/of.html', {'orderform': orderform, 'cart':cart })
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


