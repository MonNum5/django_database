# Generated by Django 3.0.6 on 2020-06-03 15:26

import databases.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('databases', '0016_auto_20200603_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='database',
            name='image',
            field=models.FileField(default='databaseImages/defaultDBImage.png', upload_to=databases.models.content_file_name),
        ),
    ]