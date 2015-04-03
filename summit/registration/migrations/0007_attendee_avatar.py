# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0006_auto_20150331_1950'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendee',
            name='avatar',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
    ]
