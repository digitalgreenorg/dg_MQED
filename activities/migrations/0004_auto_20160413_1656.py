# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0003_screening_crop_stage'),
    ]

    operations = [
        migrations.AddField(
            model_name='screening',
            name='female_attendees',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='screening',
            name='male_attendees',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
    ]
