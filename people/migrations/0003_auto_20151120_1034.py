# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_auto_20151118_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animator',
            name='father_name',
            field=models.CharField(max_length=100, editable=False, blank=True),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='animator',
            unique_together=set([('name', 'gender', 'partner')]),
        ),
    ]
