# Generated by Django 3.0.6 on 2020-05-28 20:39

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20200528_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='allowedDB',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('a', 'CRC World Fuel Survey'), ('b', 'new')], max_length=3),
        ),
    ]
