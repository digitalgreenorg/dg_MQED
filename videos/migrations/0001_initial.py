# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('geographies', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('people', '0001_initial'),
        ('programs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('time_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('time_modified', models.DateTimeField(auto_now=True, null=True)),
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('old_coco_id', models.BigIntegerField(null=True, editable=False)),
                ('language_name', models.CharField(unique=b'True', max_length=100)),
                ('user_created', models.ForeignKey(related_name='videos_language_created', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('user_modified', models.ForeignKey(related_name='videos_language_related_modified', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NonNegotiable',
            fields=[
                ('time_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('time_modified', models.DateTimeField(auto_now=True, null=True)),
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('non_negotiable', models.CharField(max_length=500)),
                ('chapter', models.CharField(max_length=500)),
                ('days_after_sowing', models.CharField(max_length=500)),
                ('physically_verifiable', models.BooleanField(default=False, db_index=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('time_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('time_modified', models.DateTimeField(auto_now=True, null=True)),
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('old_coco_id', models.BigIntegerField(null=True, editable=False)),
                ('topic_name', models.CharField(default=b'None', max_length=100)),
                ('user_created', models.ForeignKey(related_name='videos_topic_created', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('user_modified', models.ForeignKey(related_name='videos_topic_related_modified', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('time_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('time_modified', models.DateTimeField(auto_now=True, null=True)),
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('old_coco_id', models.BigIntegerField(null=True, editable=False)),
                ('title', models.CharField(max_length=200)),
                ('duration', models.TimeField(null=True, blank=True)),
                ('summary', models.TextField(blank=True)),
                ('women_featured', models.CharField(max_length=100, choices=[(b'Farming', b'Farming'), (b'Teaching', b'Teaching'), (b'Making Decisions', b'Making Decisions'), (b'Being Interviwed', b'Being Interviwed'), (b'Other Activities', b'Other Activities'), (b'Does not feature women', b'Does not feature women')])),
                ('approval_date', models.DateField(null=True, blank=True)),
                ('video_status', models.CharField(max_length=100, choices=[(b'Storyboard', b'Storyboard'), (b'Filming', b'Filming'), (b'Post Production', b'Post Production'), (b'Waiting for Approval', b'Waiting for Approval'), (b'Approved', b'Approved')])),
                ('youtubeid', models.CharField(max_length=20, blank=True)),
                ('language', models.ForeignKey(to='videos.Language')),
                ('other_persons_shown', models.ForeignKey(blank=True, to='people.Person', null=True)),
                ('partner', models.ForeignKey(verbose_name=b'Supply Partner', to='programs.Partner')),
                ('persons_shown', models.ManyToManyField(related_name='persons_shown', to='people.Person')),
                ('production_team', models.ManyToManyField(related_name='production_team', to='people.Animator')),
                ('topic', models.ForeignKey(related_name='topic', to='videos.Topic')),
                ('user_created', models.ForeignKey(related_name='videos_video_created', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('user_modified', models.ForeignKey(related_name='videos_video_related_modified', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('village', models.ForeignKey(to='geographies.Village')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='video',
            unique_together=set([('title', 'topic', 'village')]),
        ),
        migrations.AddField(
            model_name='nonnegotiable',
            name='topic',
            field=models.ForeignKey(to='videos.Topic'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='nonnegotiable',
            name='user_created',
            field=models.ForeignKey(related_name='videos_nonnegotiable_created', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='nonnegotiable',
            name='user_modified',
            field=models.ForeignKey(related_name='videos_nonnegotiable_related_modified', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
