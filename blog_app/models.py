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


class Comment(models.Model):
    content = models.CharField(max_length=280)
    social_media = models.CharField(max_length=50)  # 来自微博，facebook 或者 google+
    social_media_nickname = models.CharField(max_length=100)
    social_media_icon = models.CharField(max_length=200)
    upload_time = models.DateField()

    def __unicode__(self):
        return "来自" + self.social_media + "的" + self.social_media_nickname


class CommentReply(models.Model):
    content = models.CharField(max_length=280)  # 回复评论的内容
    social_media = models.CharField(max_length=50)  # 来自于哪里的社交媒体
    social_media_nickname = models.CharField(max_length=100)
    social_media_icon = models.CharField(max_length=200)
    upload_time = models.DateField()
    commented = models.ForeignKey(Comment)  # 被评论的评论

    # 特别注意，这个反馈是用来记录评论的
    feedback_message_url = models.CharField(max_length=300, blank=True)

    def __unicode__(self):
        return "来自" + self.social_media + "的" + self.social_media_nickname
