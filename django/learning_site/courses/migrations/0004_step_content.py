# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-31 11:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20170331_1048'),
    ]

    operations = [
        migrations.AddField(
            model_name='step',
            name='content',
            field=models.TextField(blank=True, default=''),
        ),
    ]
