# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20180822_1111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='sections',
        ),
        migrations.AddField(
            model_name='about',
            name='sections',
            field=models.ManyToManyField(to='pages.Section'),
        ),
    ]
