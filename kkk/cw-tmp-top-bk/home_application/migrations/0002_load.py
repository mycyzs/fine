# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Load',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('load_info', models.TextField(default=b'')),
                ('created_time', models.CharField(default=b'', max_length=60, null=True)),
                ('host', models.ForeignKey(to='home_application.Host')),
            ],
        ),
    ]
