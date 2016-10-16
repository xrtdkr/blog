# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=40)),
                ('subtitle', models.CharField(max_length=100)),
                ('selection', models.TextField(blank=True)),
                ('main_text', models.TextField()),
                ('category', models.CharField(max_length=20)),
                ('upload_time', models.DateTimeField(blank=True)),
            ],
        ),
    ]
