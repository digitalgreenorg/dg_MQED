# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('videos', '0001_initial'),
        ('people', '0001_initial'),
        ('geographies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonAdoptPractice',
            fields=[
                ('time_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('time_modified', models.DateTimeField(auto_now=True, null=True)),
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('old_coco_id', models.BigIntegerField(null=True, editable=False)),
                ('date_of_adoption', models.DateField()),
                ('group', models.ForeignKey(to='people.PersonGroup')),
                ('partner', models.ForeignKey(verbose_name=b'Supply Partner', to='programs.Partner')),
                ('topic', models.ForeignKey(to='videos.Topic')),
                ('user_created', models.ForeignKey(related_name='activities_personadoptpractice_created', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('user_modified', models.ForeignKey(related_name='activities_personadoptpractice_related_modified', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PersonMeetingAttendance',
            fields=[
                ('time_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('time_modified', models.DateTimeField(auto_now=True, null=True)),
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('old_coco_id', models.BigIntegerField(null=True, editable=False)),
                ('interested', models.BooleanField(db_index=True)),
                ('expressed_question', models.CharField(max_length=500, blank=True)),
                ('expressed_adoption_video', models.ForeignKey(related_name='expressed_adoption_video', blank=True, to='videos.Video', null=True)),
                ('person', models.ForeignKey(to='people.Person')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Screening',
            fields=[
                ('time_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('time_modified', models.DateTimeField(auto_now=True, null=True)),
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('old_coco_id', models.BigIntegerField(null=True, editable=False)),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('location', models.CharField(max_length=200, blank=True)),
                ('animator', models.ForeignKey(verbose_name=b'Field Officer', to='people.Animator')),
                ('farmer_groups_targeted', models.ManyToManyField(to='people.PersonGroup', verbose_name=b'Farmer Families')),
                ('farmers_attendance', models.ManyToManyField(to='people.Person', null=b'False', through='activities.PersonMeetingAttendance', blank=b'False')),
                ('partner', models.ForeignKey(verbose_name=b'Supply Partner', to='programs.Partner')),
                ('user_created', models.ForeignKey(related_name='activities_screening_created', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('user_modified', models.ForeignKey(related_name='activities_screening_related_modified', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('videoes_screened', models.ManyToManyField(to='videos.Video', verbose_name=b'Videos Screened')),
                ('village', models.ForeignKey(to='geographies.Village')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='screening',
            unique_together=set([('date', 'start_time', 'end_time', 'animator', 'village')]),
        ),
        migrations.AddField(
            model_name='personmeetingattendance',
            name='screening',
            field=models.ForeignKey(to='activities.Screening'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='personmeetingattendance',
            name='user_created',
            field=models.ForeignKey(related_name='activities_personmeetingattendance_created', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='personmeetingattendance',
            name='user_modified',
            field=models.ForeignKey(related_name='activities_personmeetingattendance_related_modified', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='personadoptpractice',
            unique_together=set([('group', 'topic', 'date_of_adoption')]),
        ),
    ]
