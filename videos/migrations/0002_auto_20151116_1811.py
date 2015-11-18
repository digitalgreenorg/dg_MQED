# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video_status',
            field=models.CharField(max_length=100, choices=[(b'Dissemination', b'Storyboard'), (b'Dissemination-Training', b'Filming'), (b'Video Production Training', b'Post Production')]),
            preserve_default=True,
        ),
    ]
