# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='monitor',
            name='create_time',
            field=models.CharField(default=b'', max_length=30, null=True),
        ),
    ]
