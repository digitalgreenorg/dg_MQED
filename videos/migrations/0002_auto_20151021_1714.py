# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_auto_20151021_1714'),
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='other_persons_shown',
            field=models.ForeignKey(default=None, to='people.Person'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='video',
            name='persons_shown',
            field=models.ForeignKey(related_name='persons_shown', default=None, to='people.Person'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='video',
            name='production_team',
            field=models.ForeignKey(default=None, to='people.Animator'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='video',
            name='video_status',
            field=models.IntegerField(default=None, choices=[(b'Storyboard', b'Storyboard'), (b'Filming', b'Filming'), (b'Post Production', b'Post Production'), (b'Completed-Waiting for Approval', b'Completed-Waiting for Approval'), (b'Completed-Approvaed', b'Completed-Approvaed')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='video',
            name='women_featured',
            field=models.CharField(default=None, max_length=100, choices=[(b'Farming', b'Farming'), (b'Teaching', b'Teaching'), (b'Making Decisions', b'Making Decisions'), (b'Being Interviwed', b'Making Decisions'), (b'Other Activities', b'Other Activities'), (b'Does not feature women', b'Does not feature women')]),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='video',
            unique_together=set([('title', 'topic', 'village')]),
        ),
        migrations.RemoveField(
            model_name='video',
            name='video_type',
        ),
        migrations.RemoveField(
            model_name='video',
            name='video_suitable_for',
        ),
        migrations.RemoveField(
            model_name='video',
            name='video_production_start_date',
        ),
        migrations.RemoveField(
            model_name='video',
            name='video_production_end_date',
        ),
        migrations.RemoveField(
            model_name='video',
            name='farmers_shown',
        ),
        migrations.RemoveField(
            model_name='video',
            name='cameraoperator',
        ),
        migrations.RemoveField(
            model_name='video',
            name='actors',
        ),
    ]
