# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0007_attendee_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendee',
            name='is_organizer',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='attendee',
            name='is_speaker',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='attendee',
            name='is_volunteer',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
