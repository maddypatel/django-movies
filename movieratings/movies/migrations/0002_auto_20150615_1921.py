# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=255)),
                ('genre', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('rating', models.IntegerField()),
                ('timestamp', models.DateTimeField()),
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
            name='user',
            field=models.OneToOneField(null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='rater',
            name='zip_code',
            field=models.CharField(max_length=10, default=10000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rating',
            name='rater',
            field=models.ForeignKey(to='movies.Rater'),
        ),
        migrations.AddField(
            model_name='movie',
            name='raters',
            field=models.ManyToManyField(through='movies.Rating', to='movies.Rater'),
        ),
    ]
