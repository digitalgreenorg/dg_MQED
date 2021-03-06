# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('time_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('time_modified', models.DateTimeField(auto_now=True, null=True)),
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('old_coco_id', models.BigIntegerField(null=True, editable=False)),
                ('block_name', models.CharField(unique=b'True', max_length=100, verbose_name=b'Taluk')),
                ('start_date', models.DateField(null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Taluk',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('time_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('time_modified', models.DateTimeField(auto_now=True, null=True)),
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('old_coco_id', models.BigIntegerField(null=True, editable=False)),
                ('country_name', models.CharField(unique=b'True', max_length=100)),
                ('start_date', models.DateField(null=True, blank=True)),
                ('user_created', models.ForeignKey(related_name='geographies_country_created', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('user_modified', models.ForeignKey(related_name='geographies_country_related_modified', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name_plural': 'countries',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('time_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('time_modified', models.DateTimeField(auto_now=True, null=True)),
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('old_coco_id', models.BigIntegerField(null=True, editable=False)),
                ('district_name', models.CharField(unique=b'True', max_length=100)),
                ('start_date', models.DateField(null=True, blank=True)),
                ('latitude', models.DecimalField(blank=True, null=True, max_digits=31, decimal_places=28, validators=[django.core.validators.MaxValueValidator(90), django.core.validators.MinValueValidator(-90)])),
                ('longitude', models.DecimalField(blank=True, null=True, max_digits=32, decimal_places=28, validators=[django.core.validators.MaxValueValidator(180), django.core.validators.MinValueValidator(-180)])),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('time_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('time_modified', models.DateTimeField(auto_now=True, null=True)),
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('old_coco_id', models.BigIntegerField(null=True, editable=False)),
                ('state_name', models.CharField(unique=b'True', max_length=100)),
                ('start_date', models.DateField(null=True, blank=True)),
                ('country', models.ForeignKey(to='geographies.Country')),
                ('user_created', models.ForeignKey(related_name='geographies_state_created', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('user_modified', models.ForeignKey(related_name='geographies_state_related_modified', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Village',
            fields=[
                ('time_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('time_modified', models.DateTimeField(auto_now=True, null=True)),
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('old_coco_id', models.BigIntegerField(null=True, editable=False)),
                ('village_name', models.CharField(max_length=100)),
                ('village_group', models.CharField(max_length=100, choices=[(b'Test Group', b'Test Group'), (b'Control Group', b'Control Group')])),
                ('start_date', models.DateField(null=True, blank=True)),
                ('latitude', models.CharField(max_length=25, null=True, blank=True)),
                ('longitude', models.CharField(max_length=25, null=True, blank=True)),
                ('census_code', models.CharField(max_length=1, null=True, blank=True)),
                ('block', models.ForeignKey(verbose_name=b'Taluk', to='geographies.Block')),
                ('user_created', models.ForeignKey(related_name='geographies_village_created', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('user_modified', models.ForeignKey(related_name='geographies_village_related_modified', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='village',
            unique_together=set([('village_name', 'block')]),
        ),
        migrations.AddField(
            model_name='district',
            name='state',
            field=models.ForeignKey(to='geographies.State'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='district',
            name='user_created',
            field=models.ForeignKey(related_name='geographies_district_created', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='district',
            name='user_modified',
            field=models.ForeignKey(related_name='geographies_district_related_modified', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='block',
            name='district',
            field=models.ForeignKey(to='geographies.District'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='block',
            name='user_created',
            field=models.ForeignKey(related_name='geographies_block_created', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='block',
            name='user_modified',
            field=models.ForeignKey(related_name='geographies_block_related_modified', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
