from django.db import models


class User(models.Model):
    username = models.CharField(max_length=250, verbose_name='Логин', null=True, blank=True)
    telegram_phone_number = models.CharField(max_length=100, verbose_name='Ссылка на телеграм', unique=True)
    name = models.CharField(max_length=150, verbose_name='Имя', null=True, blank=True)
    surname = models.CharField(max_length=150, verbose_name='Фамилия', null=True, blank=True)
    patronymic = models.CharField(max_length=150, verbose_name='Отчество', null=True, blank=True)
    citizenship = models.CharField(max_length=150, verbose_name='Гражданство', null=True, blank=True)
    appeal = models.CharField(max_length=150, verbose_name='Тип обращения', null=True, blank=True)
    contact_phone_number = models.CharField(max_length=50, verbose_name='Контактный номер телефона', null=True,
                                            blank=True)
    chat_id = models.BigIntegerField(verbose_name='ID чата', unique=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.name}'
