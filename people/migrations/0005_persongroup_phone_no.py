# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0004_auto_20151120_1134'),
    ]

    operations = [
        migrations.AddField(
            model_name='persongroup',
            name='phone_no',
            field=models.CharField(max_length=10, blank=True),
            preserve_default=True,
        ),
    ]
