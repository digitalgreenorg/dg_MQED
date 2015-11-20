# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0003_auto_20151120_1034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animator',
            name='father_name',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
    ]
