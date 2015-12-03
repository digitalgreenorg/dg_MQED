# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0005_persongroup_phone_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='persongroup',
            name='age',
            field=models.IntegerField(max_length=3, null=True, blank=True),
            preserve_default=True,
        ),
    ]
