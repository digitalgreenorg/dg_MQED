# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animatorassignedvillage',
            name='village_group',
        ),
        migrations.AlterUniqueTogether(
            name='animator',
            unique_together=set([('name', 'father_name', 'gender', 'partner')]),
        ),
        migrations.RemoveField(
            model_name='animator',
            name='district',
        ),
    ]
