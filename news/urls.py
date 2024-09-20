from django.urls import path
from .sitemap import StaticViewSitemap, DynamicViewSitemap, ServiceViewSitemap
from .views import *
from django.contrib.sitemaps.views import sitemap

sitemaps = {
    'static': StaticViewSitemap,
    'dynamic': DynamicViewSitemap,
    'service': ServiceViewSitemap
}

urlpatterns = [
    path('', index, name='home'),
    path('news/', all_news, name='news'),
    path('news/<slug:post_slug>/', get_news, name='post'),
    path('comments/', get_comments, name='comments'),
    path('service/<slug:service_slug>/', get_service, name='service'),
    path('en/', index_en, name='home_en'),
    path('en/news/', all_news_en, name='news_en'),
    path('en/news/<slug:post_slug>/', get_news_en, name='post_en'),
    path('en/comments/', get_comments_en, name='comments_en'),
    path('en/service/<slug:service_slug>/', get_service_en, name='service_en'),
    path('consent_data_processing/', get_consent_data_processing),
    path('privacy_policy/', get_privacy_policy),
    path('en/privacy_policy/', get_privacy_policy),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps})
]

# handler404 = pageNotFound

