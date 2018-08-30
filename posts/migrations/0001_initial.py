# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to=b'team/profiles')),
                ('prev_text', models.TextField(blank=True)),
                ('link', models.URLField()),
                ('active', models.BooleanField(default=False)),
                ('order', models.PositiveIntegerField(default=0, editable=False, db_index=True)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to=b'team/profiles')),
                ('prev_text', models.TextField(blank=True)),
                ('link', models.URLField()),
                ('is_local', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=False)),
                ('order', models.PositiveIntegerField(default=0, editable=False, db_index=True)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
    ]
