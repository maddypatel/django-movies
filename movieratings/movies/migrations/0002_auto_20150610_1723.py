# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('rating', models.IntegerField()),
                ('movie', models.ForeignKey(to='movies.Movie')),
            ],
        ),
        migrations.DeleteModel(
            name='Movies',
        ),
        migrations.DeleteModel(
            name='Ratings',
        ),
        migrations.RenameField(
            model_name='rater',
            old_name='userid',
            new_name='age',
        ),
        migrations.AddField(
            model_name='rater',
            name='zip_code',
            field=models.CharField(default=datetime.datetime(2015, 6, 10, 17, 23, 46, 618593, tzinfo=utc), max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rating',
            name='rater',
            field=models.ForeignKey(to='movies.Rater'),
        ),
    ]
