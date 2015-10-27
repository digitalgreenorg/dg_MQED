# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='screening',
            name='farmer_groups_targeted',
            field=models.ManyToManyField(to='people.PersonGroup', verbose_name=b'Farmer Families'),
            preserve_default=True,
        ),
    ]
