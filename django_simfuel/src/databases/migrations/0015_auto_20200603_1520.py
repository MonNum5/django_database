# Generated by Django 3.0.6 on 2020-06-03 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('databases', '0014_auto_20200603_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='database',
            name='image',
            field=models.ImageField(default='databaseImages/defaultDBImage.png', upload_to=''),
        ),
    ]
