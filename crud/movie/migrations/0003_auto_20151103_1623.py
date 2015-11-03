# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_auto_20151103_1621'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='Funny',
            new_name='funny',
        ),
    ]
