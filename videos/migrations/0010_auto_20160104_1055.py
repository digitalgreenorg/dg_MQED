# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0009_auto_20160104_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nonnegotiable',
            name='chapter',
            field=models.CharField(max_length=500, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='nonnegotiable',
            name='timing',
            field=models.CharField(max_length=500, null=True, blank=True),
            preserve_default=True,
        ),
    ]
