# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, null=True)),
                ('email', models.CharField(max_length=150, null=True)),
                ('platform', models.CharField(max_length=30, null=True)),
                ('execute_type', models.CharField(max_length=30, null=True)),
            ],
        ),
    ]
