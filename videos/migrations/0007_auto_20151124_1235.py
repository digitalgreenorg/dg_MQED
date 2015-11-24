# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0006_auto_20151124_1227'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='video_status',
            new_name='video_suitable_for',
        ),
    ]
