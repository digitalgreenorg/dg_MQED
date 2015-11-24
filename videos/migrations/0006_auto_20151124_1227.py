# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0005_remove_video_other_persons_shown'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='persons_shown',
            field=models.ManyToManyField(related_name='persons_shown', null=True, to='people.Person', blank=True),
            preserve_default=True,
        ),
    ]
