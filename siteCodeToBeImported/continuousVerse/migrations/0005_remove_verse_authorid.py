# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-30 21:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('continuousVerse', '0004_verse_authorid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='verse',
            name='authorId',
        ),
    ]
