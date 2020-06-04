# Generated by Django 3.0.6 on 2020-06-03 19:46

from django.db import migrations, models
import notebooks.models
import notebooks.validators


class Migration(migrations.Migration):

    dependencies = [
        ('notebooks', '0014_auto_20200603_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notebook',
            name='file',
            field=models.FileField(blank=True, upload_to=notebooks.models.content_file_name, validators=[notebooks.validators.validate_file_extension]),
        ),
    ]