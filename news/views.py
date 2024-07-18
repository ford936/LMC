from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render
from django.core.paginator import Paginator

from .models import News, Service, Reviews


def index(request):
    posts = News.objects.filter(is_published=True)[:3]
    services = Service.objects.filter(is_published=True)
    reviews = Reviews.objects.all()[:6]
    return render(request, 'news/index.html', context={'posts': posts, 'services': services, 'reviews': reviews})


def all_news(request):
    posts = News.objects.filter(is_published=True)
    paginator = Paginator(posts, 8)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'news/all_news.html', context={'posts': page_obj})


def get_news(request, post_slug):
    post = News.objects.filter(slug=post_slug)
    return render(request, 'news/news.html', context={'post': post})


def get_comments(request):
    reviews = Reviews.objects.all()
    return render(request, 'news/comment.html', context={'reviews': reviews})


# EN
def index_en(request):
    posts = News.objects.filter(is_published=True)[:3]
    services = Service.objects.filter(is_published=True)
    reviews = Reviews.objects.all()[:6]
    return render(request, 'news/index_en.html', context={'posts': posts, 'services': services, 'reviews': reviews})


def all_news_en(request):
    posts = News.objects.filter(is_published=True)
    paginator = Paginator(posts, 8)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'news/all_news_en.html', context={'posts': page_obj})


def get_news_en(request, post_slug):
    post = News.objects.filter(slug=post_slug)
    return render(request, 'news/news_en.html', context={'post': post})


def get_comments_en(request):
    reviews = Reviews.objects.all()
    return render(request, 'news/comment_en.html', context={'reviews': reviews})





def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')