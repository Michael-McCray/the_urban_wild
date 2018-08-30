# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Homepage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('banner_title', models.CharField(max_length=255)),
                ('banner_tagline', models.CharField(max_length=255)),
                ('banner_image', models.ImageField(upload_to=b'homepage/banner')),
                ('what_we_do_title', models.CharField(max_length=255)),
                ('what_we_do_background', models.ImageField(help_text=b'what we do section background', upload_to=b'homepage/we_do')),
                ('mission_title', models.CharField(max_length=255)),
                ('mission_text', models.TextField()),
                ('mission_background', models.ImageField(help_text=b'Mission section background', upload_to=b'homepage/mission')),
                ('published', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=False, help_text=b'activate to show on site')),
            ],
        ),
        migrations.CreateModel(
            name='What_We_Do',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('text', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to=b'stats/image', blank=True)),
                ('image_alt', models.CharField(max_length=255, blank=True)),
                ('active', models.BooleanField(default=False, help_text=b'activate to show on site')),
                ('published', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
