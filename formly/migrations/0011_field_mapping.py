# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-01-17 11:05
from __future__ import unicode_literals

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('formly', '0010_auto_20170609_0800'),
    ]

    operations = [
        migrations.AddField(
            model_name='field',
            name='mapping',
            field=jsonfield.fields.JSONField(blank=True, default={}),
        ),
    ]
