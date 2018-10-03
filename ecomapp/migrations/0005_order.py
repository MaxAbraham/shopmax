# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-09-29 10:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ecomapp', '0004_auto_20180928_1110'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=255)),
                ('buying_type', models.CharField(choices=[('With no deliveries', 'With no deliveries'), ('Delivery', 'Delivery')], max_length=40)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('comments', models.TextField()),
                ('status', models.CharField(choices=[('Accepted for processing', 'Accepted for processing'), ('Is carried out', 'Is carried out'), ('Paid', 'Paid')], max_length=100)),
                ('items', models.ManyToManyField(to='ecomapp.Cart')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
