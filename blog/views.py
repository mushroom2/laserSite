from django.shortcuts import render, get_object_or_404
from cart1.cart import Cart
from blog.models import Article
from photologue.models import *


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
    return render(request, 'blog/about.html', {'cart':cart})


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

