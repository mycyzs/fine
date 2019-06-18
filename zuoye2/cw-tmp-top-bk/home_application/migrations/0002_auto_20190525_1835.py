# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order_name', models.CharField(max_length=30)),
                ('creator', models.CharField(max_length=30)),
                ('checker', models.CharField(max_length=30)),
                ('content', models.TextField(null=True)),
                ('status', models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='server',
            name='host',
        ),
        migrations.DeleteModel(
            name='Host',
        ),
        migrations.DeleteModel(
            name='Server',
        ),
    ]
