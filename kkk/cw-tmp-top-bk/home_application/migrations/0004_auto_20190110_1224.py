# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0003_host_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='os_type',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
