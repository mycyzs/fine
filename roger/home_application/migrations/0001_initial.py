# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='monitor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('load', models.TextField()),
                ('men', models.TextField()),
                ('disk', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bk_host_innerip', models.CharField(max_length=40)),
                ('bk_host_name', models.CharField(max_length=50)),
                ('bk_cloud_id', models.CharField(max_length=30)),
                ('bk_inst_name', models.CharField(max_length=50)),
                ('bk_os_type', models.CharField(max_length=30)),
                ('bk_biz_id', models.CharField(max_length=30)),
                ('bk_biz_name', models.CharField(max_length=30)),
                ('creator', models.CharField(default=b'', max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='monitor',
            name='server',
            field=models.ForeignKey(to='home_application.Server'),
        ),
    ]
