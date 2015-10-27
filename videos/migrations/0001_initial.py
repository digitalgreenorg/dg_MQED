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
                ('topic_name', models.CharField(default=b'', max_length=100)),
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
                ('video_type', models.IntegerField(max_length=1, choices=[(1, b'Demonstration'), (2, b'Success story/ Testimonial'), (3, b'Activity Introduction'), (4, b'Discussion'), (5, b'General Awareness')])),
                ('duration', models.TimeField(null=True, blank=True)),
                ('summary', models.TextField(blank=True)),
                ('video_production_start_date', models.DateField()),
                ('video_production_end_date', models.DateField()),
                ('approval_date', models.DateField(null=True, blank=True)),
                ('video_suitable_for', models.IntegerField(choices=[(1, b'Dissemination'), (2, b'Video Production Training'), (3, b'Dissemination Training'), (4, b'Nothing'), (5, b'Pending for Approval')])),
                ('actors', models.CharField(max_length=1, choices=[(b'I', b'Individual'), (b'F', b'Family'), (b'G', b'Group')])),
                ('youtubeid', models.CharField(max_length=20, blank=True)),
                ('cameraoperator', models.ForeignKey(related_name='cameraoperator', to='people.Animator')),
                ('facilitator', models.ForeignKey(related_name='facilitator', to='people.Animator')),
                ('farmers_shown', models.ManyToManyField(to='people.Person')),
                ('language', models.ForeignKey(to='videos.Language')),
                ('partner', models.ForeignKey(verbose_name=b'company', to='programs.Partner')),
                ('topic', models.ForeignKey(to='videos.Topic')),
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
            unique_together=set([('title', 'video_production_start_date', 'video_production_end_date', 'village')]),
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
