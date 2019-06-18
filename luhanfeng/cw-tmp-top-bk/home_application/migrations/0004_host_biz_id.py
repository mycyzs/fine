# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0003_host_host_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='host',
            name='biz_id',
            field=models.IntegerField(null=True),
        ),
    ]
