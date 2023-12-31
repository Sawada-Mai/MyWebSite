# Generated by Django 4.1 on 2023-04-30 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0002_alter_album_explanation"),
    ]

    operations = [
        migrations.CreateModel(
            name="News",
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
                ("title", models.CharField(max_length=100)),
                ("date", models.DateField(verbose_name="date")),
            ],
        ),
        migrations.CreateModel(
            name="Portfolio",
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
                ("title", models.CharField(max_length=20)),
                (
                    "image",
                    models.ImageField(upload_to="portfolio/", verbose_name="image"),
                ),
                ("detail", models.CharField(max_length=50)),
                ("text1", models.TextField()),
                ("text2", models.TextField()),
            ],
        ),
    ]
