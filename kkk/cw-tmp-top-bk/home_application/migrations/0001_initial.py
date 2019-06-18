# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('host_ip', models.CharField(max_length=30)),
                ('host_name', models.CharField(max_length=30, null=True)),
                ('app_name', models.CharField(max_length=20)),
                ('app_id', models.CharField(max_length=20)),
                ('cloud_name', models.CharField(max_length=20)),
                ('cloud_id', models.CharField(max_length=20)),
                ('os_type', models.CharField(max_length=20)),
                ('disk', models.TextField(default=b'')),
                ('men', models.TextField(default=b'')),
            ],
        ),
    ]
