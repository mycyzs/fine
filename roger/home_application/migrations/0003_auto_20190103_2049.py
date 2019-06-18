# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0002_monitor_create_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='monitor',
            name='disk',
        ),
        migrations.RemoveField(
            model_name='monitor',
            name='men',
        ),
        migrations.AddField(
            model_name='server',
            name='disk',
            field=models.TextField(default=b''),
        ),
        migrations.AddField(
            model_name='server',
            name='men',
            field=models.TextField(default=b''),
        ),
    ]
