# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20180822_1122'),
    ]

    operations = [
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('banner_title', models.CharField(max_length=255)),
                ('banner_tagline', models.CharField(max_length=255)),
                ('banner_image', models.ImageField(upload_to=b'homepage/banner')),
                ('our_events_title', models.CharField(max_length=255)),
                ('local_events_title', models.CharField(max_length=255)),
                ('blog_title', models.CharField(max_length=255)),
                ('host_title', models.CharField(max_length=255)),
                ('host_text', models.TextField()),
                ('host_button_text', models.CharField(max_length=255)),
                ('host_button_link', models.URLField()),
                ('active', models.BooleanField(default=False, help_text=b'activate to show on site')),
                ('published', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
