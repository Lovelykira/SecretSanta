# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-06 13:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('santa_app', '0009_auto_20160806_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='santa_for',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
