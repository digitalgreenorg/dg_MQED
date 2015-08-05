# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animator',
            name='partner',
            field=models.ForeignKey(verbose_name=b'company', to='programs.Partner'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='partner',
            field=models.ForeignKey(verbose_name=b'company', to='programs.Partner'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='persongroup',
            name='partner',
            field=models.ForeignKey(verbose_name=b'company', to='programs.Partner'),
            preserve_default=True,
        ),
    ]
