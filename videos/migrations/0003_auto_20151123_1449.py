# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0002_auto_20151116_1811'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nonnegotiable',
            old_name='days_after_sowing',
            new_name='timing',
        ),
    ]