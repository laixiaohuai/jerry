# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-08 08:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0003_auto_20170208_0310'),
    ]

    operations = [
        migrations.AddField(
            model_name='groups',
            name='comment',
            field=models.CharField(default=django.utils.timezone.now, max_length=60),
            preserve_default=False,
        ),
    ]
