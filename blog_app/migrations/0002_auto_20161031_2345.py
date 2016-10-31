# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=280)),
                ('social_media', models.CharField(max_length=50)),
                ('social_media_nickname', models.CharField(max_length=100)),
                ('social_media_icon', models.CharField(max_length=200)),
                ('upload_time', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='CommentReply',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.CharField(max_length=280)),
                ('social_media', models.CharField(max_length=50)),
                ('social_media_nickname', models.CharField(max_length=100)),
                ('social_media_icon', models.CharField(max_length=200)),
                ('upload_time', models.DateField()),
                ('feedback_message_url', models.CharField(max_length=300, blank=True)),
                ('commented', models.ForeignKey(to='blog_app.Comment')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='read_count',
            field=models.IntegerField(default=0, blank=True),
        ),
    ]
