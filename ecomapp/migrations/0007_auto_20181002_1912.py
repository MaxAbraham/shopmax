# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-10-02 16:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0006_auto_20180929_2356'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='items',
        ),
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ecomapp.Cart'),
            preserve_default=False,
        ),
    ]
