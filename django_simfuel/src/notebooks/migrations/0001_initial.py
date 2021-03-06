# Generated by Django 3.0.6 on 2020-06-02 19:07

import django.contrib.postgres.fields.jsonb
import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='notebook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, unique=True)),
                ('created', models.DateTimeField(editable=False)),
                ('modified', models.DateTimeField()),
                ('file', models.FileField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='/Users/Clemens/Desktop/django_database/django_simfuel/src/static/notebooks'), upload_to='')),
                ('notes', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
            ],
        ),
    ]
