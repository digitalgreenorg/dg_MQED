# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0004_auto_20151124_1140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='other_persons_shown',
        ),
    ]
