# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0002_auto_20190615_1024'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='background_img',
            field=models.BinaryField(null=True),
        ),
    ]
