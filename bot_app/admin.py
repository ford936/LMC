from django.contrib import admin
from .models import *


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ('username', 'telegram_phone_number', 'name', 'surname', 'patronymic', 'citizenship', 'appeal',
              'contact_phone_number', 'chat_id')
    list_display = ['name', 'surname', 'patronymic', 'citizenship', 'appeal', 'contact_phone_number', 'username',
                    'telegram_phone_number']
    search_fields = ['appeal']
