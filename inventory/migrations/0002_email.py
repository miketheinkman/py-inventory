# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-26 18:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monday', models.BooleanField()),
                ('tuesday', models.BooleanField()),
                ('wednesday', models.BooleanField()),
                ('thursday', models.BooleanField()),
                ('friday', models.BooleanField()),
                ('saturday', models.BooleanField()),
                ('sunday', models.BooleanField()),
                ('monday_time', models.TimeField(blank=True, verbose_name='Email Time')),
                ('tuesday_time', models.TimeField(blank=True, verbose_name='Email Time')),
                ('wednesday_time', models.TimeField(blank=True, verbose_name='Email Time')),
                ('thursday_time', models.TimeField(blank=True, verbose_name='Email Time')),
                ('friday_time', models.TimeField(blank=True, verbose_name='Email Time')),
                ('saturday_time', models.TimeField(blank=True, verbose_name='Email Time')),
                ('sunday_time', models.TimeField(blank=True, verbose_name='Email Time')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Vendor')),
            ],
        ),
    ]
