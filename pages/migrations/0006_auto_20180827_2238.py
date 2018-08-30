# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20180827_2135'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accordion_Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('active', models.BooleanField(default=False, help_text=b'activate to show on site')),
                ('published', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RenameField(
            model_name='about',
            old_name='banner_tagline',
            new_name='team_tagline',
        ),
        migrations.AddField(
            model_name='about',
            name='who_we_are_tagline',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='about',
            name='who_we_are_text',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='about',
            name='who_we_are_title',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='about',
            name='accordion_Items',
            field=models.ManyToManyField(to='pages.Accordion_Item'),
        ),
    ]
