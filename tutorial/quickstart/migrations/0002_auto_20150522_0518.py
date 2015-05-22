# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quickstart',
            old_name='styles',
            new_name='style',
        ),
    ]
