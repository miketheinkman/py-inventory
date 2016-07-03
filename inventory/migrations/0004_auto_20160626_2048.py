# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-26 20:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20160626_2003'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_use_quantity',
            field=models.IntegerField(default=1),
        ),
    ]
