# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-05 18:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='car',
            options={'ordering': ['-brand', 'pattern', '-year', '-price'], 'verbose_name': 'Car', 'verbose_name_plural': 'Cars'},
        ),
        migrations.AlterModelTable(
            name='car',
            table='car',
        ),
    ]
