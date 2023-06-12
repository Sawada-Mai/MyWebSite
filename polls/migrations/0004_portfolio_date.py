# Generated by Django 4.1 on 2023-05-01 06:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0003_news_portfolio"),
    ]

    operations = [
        migrations.AddField(
            model_name="portfolio",
            name="date",
            field=models.DateField(
                default=django.utils.timezone.now, verbose_name="date"
            ),
        ),
    ]