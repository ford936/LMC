from django.contrib import admin

from .models import *


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(News, NewsAdmin)


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'price', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Service, ServiceAdmin)


class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'url')
    list_filter = ('title',)


admin.site.register(Reviews, ReviewsAdmin)
