from django.db import models
from django.urls import reverse
import uuid


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    title_en = models.CharField(max_length=255, blank=True, verbose_name="Заголовок английский")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=False, verbose_name="Текст статьи")
    content_en = models.TextField(blank=True, verbose_name="Текст статьи английский")
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name="Фото")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-time_create', 'title']


class Service(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    title_en = models.CharField(max_length=255, blank=True, verbose_name="Заголовок английский")
    slug = models.SlugField(max_length=255, db_index=True, verbose_name="URL")
    price = models.CharField(max_length=50, blank=False, verbose_name="Цена")
    content = models.TextField(blank=False, verbose_name="Текст услуги")
    content_en = models.TextField(blank=True, verbose_name="Текст услуги английский")
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name="Фото")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('service', kwargs={'service_slug': self.slug})

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        ordering = ['-time_create', 'title']


class Reviews(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название отзыва")
    url = models.TextField(blank=False, verbose_name="Ссылка на отзыв")
    video = models.FileField(upload_to='video/%Y/%m/%d/', verbose_name="Видео")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['title']
