from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.shortcuts import render, get_object_or_404
from cart1.cart import Cart
from blog.models import Article, Partners
from photologue.models import *
from blog.forms import SimpleForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect


def home(request):
    news = Article.objects.order_by('-pub_day')[:5]
    imgs = Photo.objects.on_site().is_public()[:5]
    cart= Cart(request)
    context={
        'news': news,
        'imgs': imgs,
        'cart': cart
    }
    return render(request, 'blog/home.html', context)


def about(request):
    cart= Cart(request)
    partners= Partners.objects.all()
    form = SimpleForm(request.POST)
    return render(request, 'blog/about.html', {'cart': cart, 'partners': partners, 'form': form})


def show_partners(request, partner_id):
    partner = get_object_or_404(Partners ,id= partner_id)
    return render(request, 'blog/partner.html', {'partner': partner})


def xxx(request):
    articles = Article.objects.order_by('-pub_day')
    cart= Cart(request)
    context={
        'articles': articles,
        'cart': cart,
    }

    return render(request, 'blog/xxx.html', context)


def show_article(request, article_id):
    article = get_object_or_404(Article, id= article_id)
    cart= Cart(request)
    return render(request, 'blog/article.html', {'article': article, 'cart': cart})


def mysimpleform(request):

    if request.method == 'POST':
        form = SimpleForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username'] + ' from ' + str(form.cleaned_data['sender'])
            sender = form.cleaned_data['sender']
            message = form.cleaned_data['message']
            copy = form.cleaned_data['copy']

            recipients = ['avi.upsale@gmail.com']

            if copy == True:
                recipients.append(sender)
            try:
                send_mail(username, message, sender, recipients)
            except BadHeaderError:
                return HttpResponse('something goes wrong ;(')
            return HttpResponseRedirect('/thanks')

    else:
        form = SimpleForm()
    return render(request, 'blog/simpleform.html', {'form': form, 'username': auth.get_user(request).username})


def thenks(request):
    thenks = 'thenks'
    context = {'thenks': thenks}
    return render(request, 'blog/thenks.html', context)

def userauth(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/about/')
            else:
                return HttpResponse("Your sferalaser account is disabled.")
        else:
            print('невірні данні: {0}, {1}'.format(username, password))
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'blog/userlogin.html', {})
