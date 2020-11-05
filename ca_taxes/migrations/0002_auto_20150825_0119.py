# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ca_taxes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='catax',
            options={'ordering': ['city'], 'verbose_name': 'CA Tax', 'verbose_name_plural': 'CA Taxes'},
        ),
    ]
