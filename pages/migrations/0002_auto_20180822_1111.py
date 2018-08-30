# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('banner_title', models.CharField(max_length=255)),
                ('banner_tagline', models.CharField(max_length=255)),
                ('banner_image', models.ImageField(upload_to=b'homepage/banner')),
                ('team_title', models.CharField(max_length=255)),
                ('active', models.BooleanField(default=False, help_text=b'activate to show on site')),
                ('published', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('section_title', models.CharField(max_length=255)),
                ('left_title', models.CharField(max_length=255)),
                ('left_text', models.TextField()),
                ('left_image', models.ImageField(upload_to=b'section/left')),
                ('right_title', models.CharField(max_length=255)),
                ('right_text', models.TextField()),
                ('right_image', models.ImageField(upload_to=b'section/right')),
                ('active', models.BooleanField(default=False, help_text=b'activate to show on site')),
                ('published', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='about',
            name='sections',
            field=models.ForeignKey(to='pages.Section'),
        ),
    ]
