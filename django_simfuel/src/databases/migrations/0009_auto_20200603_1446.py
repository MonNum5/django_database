# Generated by Django 3.0.6 on 2020-06-03 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('databases', '0008_auto_20200603_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='database',
            name='image',
            field=models.ImageField(blank=True, default='defaultDBImage.png', null=True, upload_to=''),
        ),
    ]
