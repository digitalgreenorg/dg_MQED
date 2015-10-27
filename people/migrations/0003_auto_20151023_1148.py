# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_auto_20151021_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animator',
            name='district',
            field=models.ForeignKey(default=None, to='geographies.District'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='animator',
            name='trained_in_video_production',
            field=models.CharField(max_length=1, choices=[(b'N', b'No'), (b'Y', b'Yes')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='animator',
            name='trained_in_video_screening',
            field=models.CharField(max_length=1, choices=[(b'N', b'No'), (b'Y', b'Yes')]),
            preserve_default=True,
        ),
    ]
