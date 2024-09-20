from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

from .models import News, Service


class StaticViewSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 1.0

    def items(self):
        return ['home', 'home_en']

    def location(self, item):
        return reverse(item)


class DynamicViewSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.9

    def items(self):
        return News.objects.all()


class ServiceViewSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.9

    def items(self):
        return Service.objects.all()