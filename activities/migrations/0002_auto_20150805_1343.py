# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personadoptpractice',
            name='non_negotiable_check',
        ),
        migrations.RemoveField(
            model_name='personadoptpractice',
            name='verification_status',
        ),
        migrations.RemoveField(
            model_name='personadoptpractice',
            name='verified_by',
        ),
        migrations.RemoveField(
            model_name='screening',
            name='observation_status',
        ),
        migrations.RemoveField(
            model_name='screening',
            name='observer',
        ),
        migrations.RemoveField(
            model_name='screening',
            name='screening_grade',
        ),
        migrations.AlterField(
            model_name='personadoptpractice',
            name='partner',
            field=models.ForeignKey(verbose_name=b'company', to='programs.Partner'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='screening',
            name='partner',
            field=models.ForeignKey(verbose_name=b'company', to='programs.Partner'),
            preserve_default=True,
        ),
    ]
