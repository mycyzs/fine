# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServerPerformance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cpu_usage', models.FloatField()),
                ('mem_usage', models.FloatField()),
                ('disk_usage', models.FloatField()),
                ('when_created', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Servers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip_address', models.CharField(max_length=100)),
                ('cloud_id', models.IntegerField(default=0)),
                ('app_id', models.IntegerField(default=0)),
                ('os_name', models.CharField(max_length=200)),
                ('cloud_name', models.CharField(max_length=100)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='serverperformance',
            name='server',
            field=models.ForeignKey(to='home_application.Servers'),
        ),
    ]
