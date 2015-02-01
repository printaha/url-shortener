# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='URL',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('short_id', models.CharField(max_length=8, unique=True)),
                ('full_URL', models.CharField(max_length=2048)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
