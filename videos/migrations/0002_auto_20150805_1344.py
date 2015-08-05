# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='review_status',
        ),
        migrations.RemoveField(
            model_name='video',
            name='reviewer',
        ),
        migrations.RemoveField(
            model_name='video',
            name='video_grade',
        ),
        migrations.AlterField(
            model_name='video',
            name='partner',
            field=models.ForeignKey(verbose_name=b'company', to='programs.Partner'),
            preserve_default=True,
        ),
    ]
