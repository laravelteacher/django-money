# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-09-22 16:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangobin', '0006_remove_snippet_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='snippet',
            name='language',
        ),
    ]