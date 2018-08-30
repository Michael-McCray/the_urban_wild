# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
        ('pages', '0004_community'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('tagline', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to=b'stats/image', blank=True)),
                ('image_alt', models.CharField(max_length=255, blank=True)),
                ('button_active', models.BooleanField(default=False, help_text=b'activate to show on site')),
                ('button1_text', models.CharField(max_length=255, blank=True)),
                ('button1_link', models.URLField(blank=True)),
                ('button2_text', models.CharField(max_length=255, blank=True)),
                ('button2_link', models.URLField(blank=True)),
                ('active', models.BooleanField(default=False, help_text=b'activate to show on site')),
                ('published', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='banner_tagline',
            new_name='members_tagline',
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='banner_title',
            new_name='members_title',
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='what_we_do_background',
            new_name='what_we_do_center',
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='mission_title',
            new_name='what_we_do_tagline',
        ),
        migrations.RemoveField(
            model_name='about',
            name='sections',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='mission_background',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='mission_text',
        ),
        migrations.RemoveField(
            model_name='what_we_do',
            name='image',
        ),
        migrations.RemoveField(
            model_name='what_we_do',
            name='image_alt',
        ),
        migrations.AddField(
            model_name='about',
            name='members',
            field=models.ManyToManyField(to='team.Team'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='members',
            field=models.ManyToManyField(to='team.Team'),
        ),
        migrations.AddField(
            model_name='what_we_do',
            name='link',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='what_we_do',
            name='right_side',
            field=models.BooleanField(default=False, help_text=b'activate to show on right side'),
        ),
        migrations.DeleteModel(
            name='Section',
        ),
        migrations.AddField(
            model_name='homepage',
            name='banner_slides',
            field=models.ManyToManyField(to='pages.Slide'),
        ),
    ]
