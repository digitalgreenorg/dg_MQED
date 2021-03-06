# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('programs', '0001_initial'),
        ('geographies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animator',
            fields=[
                ('time_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('time_modified', models.DateTimeField(auto_now=True, null=True)),
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('old_coco_id', models.BigIntegerField(null=True, editable=False)),
                ('name', models.CharField(max_length=100)),
                ('father_name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('phone_no', models.CharField(max_length=100, blank=True)),
                ('trained_in_video_production', models.CharField(max_length=1, choices=[(b'N', b'No'), (b'Y', b'Yes')])),
                ('trained_in_video_screening', models.CharField(max_length=1, choices=[(b'N', b'No'), (b'Y', b'Yes')])),
                ('total_adoptions', models.PositiveIntegerField(default=0, editable=False, blank=True)),
            ],
            options={
                'verbose_name': 'Field Officer',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AnimatorAssignedVillage',
            fields=[
                ('time_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('time_modified', models.DateTimeField(auto_now=True, null=True)),
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('village_group', models.CharField(max_length=100, choices=[(b'Test Group', b'Test Group'), (b'Control Group', b'Control Group')])),
                ('start_date', models.DateField(null=True, blank=True)),
                ('animator', models.ForeignKey(to='people.Animator')),
                ('user_created', models.ForeignKey(related_name='people_animatorassignedvillage_created', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('user_modified', models.ForeignKey(related_name='people_animatorassignedvillage_related_modified', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('village', models.ForeignKey(to='geographies.Village')),
            ],
            options={
                'verbose_name': 'Field officer assigned village',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('time_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('time_modified', models.DateTimeField(auto_now=True, null=True)),
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('old_coco_id', models.BigIntegerField(null=True, editable=False)),
                ('person_name', models.CharField(max_length=100)),
                ('father_name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('age', models.IntegerField(max_length=3, null=True, blank=True)),
                ('relation_farmer_family', models.CharField(blank=True, max_length=100, null=True, choices=[(b'Family Member', b'Family Member'), (b'Hired Labourer', b'Hired Labourer'), (b'Other', b'Other')])),
                ('other_profession', models.CharField(max_length=100, null=True, blank=True)),
                ('phone_no', models.CharField(max_length=10, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PersonGroup',
            fields=[
                ('time_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('time_modified', models.DateTimeField(auto_now=True, null=True)),
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('old_coco_id', models.BigIntegerField(null=True, editable=False)),
                ('name', models.CharField(max_length=100)),
                ('father_name', models.CharField(max_length=100)),
                ('aadhar_id', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('partner', models.ForeignKey(verbose_name=b'Supply Partner', to='programs.Partner')),
                ('user_created', models.ForeignKey(related_name='people_persongroup_created', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('user_modified', models.ForeignKey(related_name='people_persongroup_related_modified', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('village', models.ForeignKey(to='geographies.Village')),
            ],
            options={
                'verbose_name': 'Farmer Family',
                'verbose_name_plural': 'Farmer Families',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='persongroup',
            unique_together=set([('name', 'father_name', 'village')]),
        ),
        migrations.AddField(
            model_name='person',
            name='group',
            field=models.ForeignKey(verbose_name=b'Farmer Family', blank=True, to='people.PersonGroup', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='person',
            name='partner',
            field=models.ForeignKey(verbose_name=b'Supply Partner', to='programs.Partner'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='person',
            name='user_created',
            field=models.ForeignKey(related_name='people_person_created', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='person',
            name='user_modified',
            field=models.ForeignKey(related_name='people_person_related_modified', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='person',
            name='village',
            field=models.ForeignKey(to='geographies.Village'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='person',
            unique_together=set([('person_name', 'father_name', 'village')]),
        ),
        migrations.AddField(
            model_name='animator',
            name='assigned_villages',
            field=models.ManyToManyField(related_name='assigned_villages', null=True, through='people.AnimatorAssignedVillage', to='geographies.Village', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='animator',
            name='district',
            field=models.ForeignKey(to='geographies.District'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='animator',
            name='partner',
            field=models.ForeignKey(verbose_name=b'Supply Partner', to='programs.Partner'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='animator',
            name='user_created',
            field=models.ForeignKey(related_name='people_animator_created', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='animator',
            name='user_modified',
            field=models.ForeignKey(related_name='people_animator_related_modified', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='animator',
            unique_together=set([('name', 'gender', 'partner', 'district')]),
        ),
    ]
