# Generated by Django 3.0.6 on 2020-05-26 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0008_search_searchdate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='search',
            name='searchDate',
        ),
    ]
