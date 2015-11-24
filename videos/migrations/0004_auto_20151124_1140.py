# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0003_auto_20151123_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video_status',
            field=models.CharField(max_length=100, choices=[(b'Dissemination', b'Dissemination'), (b'Dissemination-Training', b'Dissemination-Training'), (b'Video Production Training', b'Video Production Training')]),
            preserve_default=True,
        ),
    ]
