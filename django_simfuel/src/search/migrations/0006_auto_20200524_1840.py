# Generated by Django 3.0.6 on 2020-05-24 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0005_search_searchdate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='search',
            name='searchDate',
        ),
        migrations.AlterField(
            model_name='search',
            name='search',
            field=models.CharField(blank=True, max_length=120),
        ),
    ]
