# Generated by Django 3.2.5 on 2021-08-07 12:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listitems', '0002_auto_20210726_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='deadline',
            field=models.DateField(default=datetime.date(2021, 8, 21), max_length=100, verbose_name='期日'),
        ),
        migrations.AlterField(
            model_name='item',
            name='photo',
            field=models.FileField(upload_to='images/', verbose_name='写真'),
        ),
    ]