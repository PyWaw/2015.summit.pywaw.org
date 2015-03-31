# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0005_auto_20150321_2236'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendee',
            name='admin_notes',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='attendee',
            name='company_city',
            field=models.CharField(blank=True, max_length=500),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='attendee',
            name='company_post_code',
            field=models.CharField(blank=True, max_length=500),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='attendee',
            name='invoice_sent',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='attendee',
            name='company_nip',
            field=models.CharField(blank=True, max_length=15, verbose_name='Company VATIN (NIP)'),
            preserve_default=True,
        ),
    ]
