# Generated by Django 5.0.6 on 2024-06-30 21:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0003_service"),
    ]

    operations = [
        migrations.CreateModel(
            name="Reviews",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(max_length=255, verbose_name="Название отзыва"),
                ),
                ("url", models.TextField(verbose_name="Ссылка на отзыв")),
            ],
            options={
                "verbose_name": "Отзыв",
                "verbose_name_plural": "Отзывы",
                "ordering": ["title"],
            },
        ),
        migrations.AlterModelOptions(
            name="news",
            options={
                "ordering": ["-time_create", "title"],
                "verbose_name": "Новость",
                "verbose_name_plural": "Новости",
            },
        ),
        migrations.AlterModelOptions(
            name="service",
            options={
                "ordering": ["-time_create", "title"],
                "verbose_name": "Услуга",
                "verbose_name_plural": "Услуги",
            },
        ),
    ]
