# coding: utf-8

from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=40)  # 文章标题
    subtitle = models.CharField(max_length=100)  # 副标题
    selection = models.TextField(blank=True)  # selection是节选
    main_text = models.TextField()  # 正文
    category = models.CharField(max_length=20)  # 所属标签
    upload_time = models.DateTimeField(blank=True)  # 上传时间
    read_count = models.IntegerField(default=0, blank=True)

    def __unicode__(self):
        return self.title


class Category(models.Model):
    '''保留类，用来以后扩展使用Category'''

