# Generated by Django 5.0.6 on 2024-09-15 09:31

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0005_reviews_video"),
    ]

    operations = [
        migrations.AddField(
            model_name="service",
            name="slug",
            field=models.SlugField(
                default=uuid.UUID("4fed5066-e930-4b47-bd9f-9d2dea418050"),
                max_length=255,
                verbose_name="URL",
            ),
        ),
    ]
