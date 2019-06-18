# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='servers',
            name='created_by',
            field=models.CharField(default=b'', max_length=100),
        ),
    ]
