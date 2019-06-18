# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=10)),
                ('mail', models.CharField(default=b'', max_length=100)),
                ('department', models.CharField(default='\u4ea7\u54c1\u7814\u53d1\u90e8', max_length=50)),
            ],
        ),
    ]
