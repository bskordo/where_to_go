# Generated by Django 3.0.7 on 2020-09-25 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_auto_20200923_0836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(upload_to='', verbose_name='Фотографие'),
        ),
    ]
