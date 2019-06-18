# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0003_auto_20190525_2018'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('check_status', models.CharField(max_length=30)),
                ('comment', models.TextField(null=True)),
                ('order', models.ForeignKey(to='home_application.Order')),
            ],
        ),
    ]
