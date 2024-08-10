from django.urls import path
from .sitemap import StaticViewSitemap, DynamicViewSitemap
from .views import index, get_news, all_news, get_comments, index_en, get_news_en, all_news_en, get_comments_en
from django.contrib.sitemaps.views import sitemap

sitemaps = {
    'static': StaticViewSitemap,
    'dynamic': DynamicViewSitemap
}

urlpatterns = [
    path('', index, name='home'),
    path('news/', all_news, name='news'),
    path('news/<slug:post_slug>/', get_news, name='post'),
    path('comments/', get_comments, name='comments'),
    path('en/', index_en, name='home_en'),
    path('en/news/', all_news_en, name='news_en'),
    path('en/news/<slug:post_slug>/', get_news_en, name='post_en'),
    path('en/comments/', get_comments_en, name='comments_en'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps})
]

# handler404 = pageNotFound

