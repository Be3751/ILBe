# Generated by Django 3.2.4 on 2021-07-26 02:50

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listitems', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='deadline',
            field=models.DateField(default=datetime.date(2021, 8, 9), max_length=100, verbose_name='期日'),
        ),
        migrations.AlterField(
            model_name='item',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='listitems.owner', verbose_name='持ち主'),
        ),
    ]
