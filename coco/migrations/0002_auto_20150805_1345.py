# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coco', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cocouser',
            name='partner',
            field=models.ForeignKey(verbose_name=b'company', to='programs.Partner'),
            preserve_default=True,
        ),
    ]
