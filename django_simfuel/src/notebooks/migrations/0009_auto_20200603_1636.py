# Generated by Django 3.0.6 on 2020-06-03 16:36

from django.db import migrations, models
import notebooks.models


class Migration(migrations.Migration):

    dependencies = [
        ('notebooks', '0008_auto_20200603_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notebook',
            name='file',
            field=models.FileField(default='notebooksTest.ipynb', upload_to=notebooks.models.content_file_name),
        ),
    ]