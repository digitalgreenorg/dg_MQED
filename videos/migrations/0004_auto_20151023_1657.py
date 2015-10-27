# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0003_auto_20151023_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='production_team',
            field=models.ForeignKey(to='people.Animator', to_field=b'production_team'),
            preserve_default=True,
        ),
    ]
