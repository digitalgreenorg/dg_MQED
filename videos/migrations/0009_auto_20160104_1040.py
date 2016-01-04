# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0008_auto_20151201_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nonnegotiable',
            name='non_negotiable',
            field=models.CharField(max_length=1000),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='topic',
            name='topic_name',
            field=models.CharField(default=b'None', max_length=1000),
            preserve_default=True,
        ),
    ]
