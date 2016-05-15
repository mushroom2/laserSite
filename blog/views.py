from django.shortcuts import render, get_object_or_404
from django.shortcuts import render_to_response
from blog.models import Article
from photologue.models import *


def home(request):
    news = Article.objects.order_by('-pub_day')[:5]
    imgs = Photo.objects.on_site().is_public()[:5]
    context={
        'news': news,
        'imgs': imgs,
    }


    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')


def xxx(request):
    articles = Article.objects.order_by('-pub_day')
    context={
        'articles': articles
    }


    return render(request, 'blog/xxx.html', context)

def show_article(request, article_id):
    article = get_object_or_404(Article, id= article_id)
    return render(request, 'blog/article.html', {'article': article})

