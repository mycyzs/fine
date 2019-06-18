# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0002_auto_20190525_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='creator',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
