# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-06 13:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('santa_app', '0005_myuser_santa_for'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='santa_for',
            field=models.OneToOneField(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
