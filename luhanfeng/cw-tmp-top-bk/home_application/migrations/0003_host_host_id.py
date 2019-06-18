# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0002_host'),
    ]

    operations = [
        migrations.AddField(
            model_name='host',
            name='host_id',
            field=models.IntegerField(null=True),
        ),
    ]
