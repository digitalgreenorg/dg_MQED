# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0007_auto_20151124_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='women_featured',
            field=models.CharField(max_length=100, choices=[(b'N', b'No'), (b'Y', b'Yes')]),
            preserve_default=True,
        ),
    ]
