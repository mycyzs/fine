# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, null=True)),
                ('content', models.TextField(null=True)),
                ('comment', models.TextField(null=True)),
                ('biz', models.CharField(max_length=30, null=True)),
                ('creator', models.CharField(max_length=30, null=True)),
                ('when_created', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Total',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.CharField(max_length=50, null=True)),
                ('sum', models.IntegerField(null=True)),
                ('book', models.ForeignKey(to='home_application.Book')),
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
