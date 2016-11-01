# coding=utf-8


from django.db import models


class Comment(models.Model):
    topic_id = models.CharField(max_length=20)
    content = models.CharField(max_length=280)

    social_media = models.CharField(max_length=50)  # 来自微博，facebook 或者 google+
    social_media_nickname = models.CharField(max_length=100)
    social_media_icon = models.CharField(max_length=200)
    social_media_url = models.CharField(max_length=200)

    upload_time = models.DateField()

    def __unicode__(self):
        return "来自" + self.social_media + "的" + self.social_media_nickname


class CommentReply(models.Model):
    topic_id = models.CharField(max_length=30)
    dst_topic_id = models.CharField(max_length=30)

    content = models.CharField(max_length=280)  # 回复评论的内容

    social_media = models.CharField(max_length=50)  # 来自于哪里的社交媒体
    social_media_nickname = models.CharField(max_length=100)
    social_media_icon = models.CharField(max_length=200)
    social_media_url = models.CharField(max_length=200)

    upload_time = models.DateField()
    commented = models.ForeignKey(Comment)  # 属于哪个大类

    # 特别注意，这个反馈是用来记录评论的链接
    feedback_message_url = models.CharField(max_length=300, blank=True)

    def __unicode__(self):
        return "来自" + self.social_media + "的" + self.social_media_nickname + "的回复"

# Create your models here.
