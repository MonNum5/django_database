# Generated by Django 3.0.6 on 2020-05-26 18:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0010_search_searchdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search',
            name='searchDate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
