# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-03-27 11:55
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0032_ltiexercise_service_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='learningobject',
            name='url',
            field=models.CharField(help_text='Input an URL identifier for this object.', max_length=255, validators=[django.core.validators.RegexValidator(message='URL keys may consist of alphanumeric characters, hyphen and period.', regex=re.compile('^\\w[\\w\\-\\.]*$', 32))]),
        ),
    ]
