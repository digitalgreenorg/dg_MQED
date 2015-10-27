# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geographies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='village',
            name='village_group',
            field=models.CharField(default=None, max_length=100, choices=[(b'Test Group', b'Test Group'), (b'Control Group', b'Control Group')]),
            preserve_default=False,
        ),
    ]
