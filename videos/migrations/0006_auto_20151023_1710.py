# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0005_auto_20151023_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='production_team',
            field=models.ForeignKey(to='people.Animator'),
            preserve_default=True,
        ),
    ]
