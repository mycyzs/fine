# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip', models.CharField(max_length=50, null=True)),
                ('life_time', models.CharField(max_length=50, null=True)),
                ('cloud', models.CharField(max_length=30, null=True)),
                ('task_id', models.ForeignKey(to='home_application.Task')),
            ],
        ),
    ]
