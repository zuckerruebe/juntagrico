# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-01 21:06
from __future__ import unicode_literals

from django.db import migrations, models
import my_ortoloco.helpers


class Migration(migrations.Migration):

    dependencies = [
        ('my_ortoloco', '0031_auto_20170301_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abo',
            name='start_date',
            field=models.DateField(default=my_ortoloco.helpers.start_of_next_year, verbose_name=b'Gew\xc3\xbcnschtes Startdatum'),
        ),
    ]
