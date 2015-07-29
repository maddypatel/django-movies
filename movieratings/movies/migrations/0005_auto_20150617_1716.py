# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_auto_20150615_2046'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='raters',
            field=models.ManyToManyField(to='movies.Rater', through='movies.Rating'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
