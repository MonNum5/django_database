# Generated by Django 3.0.6 on 2020-05-31 21:01

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0021_auto_20200531_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='allowedDB',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Brazilfuel', 'Brazil fuels'), ('CRCfuels', 'CRC World Fuel Survey')], max_length=19),
        ),
    ]
