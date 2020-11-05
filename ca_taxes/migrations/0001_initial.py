# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CATax',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('city', models.CharField(max_length=100, db_index=True)),
                ('rate', models.DecimalField(max_digits=6, decimal_places=4)),
                ('county', models.CharField(max_length=100, db_index=True)),
            ],
            options={
                'ordering': ['city'],
            },
        ),
    ]
