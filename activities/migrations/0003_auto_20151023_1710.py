# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0002_auto_20151023_1148'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personadoptpractice',
            old_name='topics',
            new_name='topic',
        ),
        migrations.AlterUniqueTogether(
            name='personadoptpractice',
            unique_together=set([('person', 'topic', 'date_of_adoption')]),
        ),
    ]
