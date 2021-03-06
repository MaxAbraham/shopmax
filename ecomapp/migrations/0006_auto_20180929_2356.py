# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-09-29 20:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0005_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='buying_type',
            field=models.CharField(choices=[('With no deliveries', 'With no deliveries'), ('Delivery', 'Delivery')], default='With no deliveries', max_length=40),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Accepted for processing', 'Accepted for processing'), ('Is carried out', 'Is carried out'), ('Paid', 'Paid')], default='Accepted for processing', max_length=100),
        ),
    ]
