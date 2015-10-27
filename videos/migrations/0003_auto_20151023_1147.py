# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0002_auto_20151021_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='other_persons_shown',
            field=models.ForeignKey(blank=True, to='people.Person', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='video',
            name='video_status',
            field=models.CharField(max_length=100, choices=[(b'Storyboard', b'Storyboard'), (b'Filming', b'Filming'), (b'Post Production', b'Post Production'), (b'Completed-Waiting for Approval', b'Completed-Waiting for Approval'), (b'Completed-Approvaed', b'Completed-Approvaed')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='video',
            name='women_featured',
            field=models.CharField(max_length=100, choices=[(b'Farming', b'Farming'), (b'Teaching', b'Teaching'), (b'Making Decisions', b'Making Decisions'), (b'Being Interviwed', b'Being Interviwed'), (b'Other Activities', b'Other Activities'), (b'Does not feature women', b'Does not feature women')]),
            preserve_default=True,
        ),
    ]
