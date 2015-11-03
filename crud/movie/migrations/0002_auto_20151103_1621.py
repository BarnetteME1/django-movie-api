# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.datetime_safe


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='Funny',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='movie',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.datetime_safe.datetime.now),
            preserve_default=False,
        ),
    ]
