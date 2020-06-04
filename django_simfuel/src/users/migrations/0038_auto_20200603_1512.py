# Generated by Django 3.0.6 on 2020-06-03 15:12

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0037_auto_20200603_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='allowedDB',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('a', 'a'), ('1', '5')], max_length=100),
        ),
    ]
