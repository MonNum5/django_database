# Generated by Django 3.0.6 on 2020-05-31 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('databases', '0003_auto_20200531_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='database',
            name='image',
            field=models.ImageField(blank=True, default='static/images/defaultDBImage.png', null=True, upload_to=''),
        ),
    ]
