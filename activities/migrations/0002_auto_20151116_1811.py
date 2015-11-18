# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
        ('activities', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='personadoptpractice',
            name='animator',
            field=models.ForeignKey(default=None, verbose_name=b'Field Officer', to='people.Animator'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='personadoptpractice',
            name='group',
            field=models.ForeignKey(verbose_name=b'Farmer Family', to='people.PersonGroup'),
            preserve_default=True,
        ),
    ]
