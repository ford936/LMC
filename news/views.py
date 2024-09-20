from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.decorators.http import require_GET

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
    if len(post) == 0:
        return render(request, 'news/error.html', status=404)
    return render(request, 'news/news.html', context={'post': post})


def get_comments(request):
    reviews = Reviews.objects.all()
    return render(request, 'news/comment.html', context={'reviews': reviews})


def get_service(request, service_slug):
    service = Service.objects.filter(slug=service_slug)
    if len(service) == 0:
        return render(request, 'news/error.html', status=404)
    return render(request, 'news/service.html', context={'service': service})


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
    if len(post) == 0:
        return render(request, 'news/error.html', status=404)
    return render(request, 'news/news_en.html', context={'post': post})


def get_comments_en(request):
    reviews = Reviews.objects.all()
    return render(request, 'news/comment_en.html', context={'reviews': reviews})


def get_service_en(request, service_slug):
    service = Service.objects.filter(slug=service_slug)
    if len(service) == 0:
        return render(request, 'news/error.html', status=404)
    return render(request, 'news/service_en.html', context={'service': service})


def get_consent_data_processing(request):
    return render(request, 'news/consent_data_processing.html')


def get_privacy_policy(request):
    return render(request, 'news/privacy_policy.html')


def page_not_found(requests, exception):
    return render(requests, 'news/error.html', status=404)
    # return HttpResponseNotFound('<h1>Страница не найдена</h1>')


@require_GET
def robots_txt(request):
    lines = [
        "User-Agent: *",
        "Disallow: /admin/",
        "Disallow: /private/",
        "Disallow: /temp/",
        "Allow: /public/",
        "Allow: /images/",
        "Sitemap: https://lmc-mos.ru/sitemap.xml",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")


def sitemap(request):
    return render(request, 'news/sitemap.xml')
