from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class AboutMe(models.Model):
    """
    自我简介
    """
    id = models.AutoField(primary_key=True)
    summary = RichTextUploadingField('摘要')  # 摘要
    content = RichTextUploadingField('正文')  # 正文
    create_at = models.DateTimeField('发布时间')  # 发布时间

    def __str__(self):
        return '自我简介'  # 后台显示标题

    class Meta:
        verbose_name = '自我简介'
        verbose_name_plural = "自我简介"  # 类的复数


class Ziyu(models.Model):
    """
    喃喃自语
    """
    id = models.AutoField(primary_key=True)
    title = models.CharField('标题', max_length=200, null=True, blank=True)
    content = RichTextUploadingField('正文')  # 正文
    create_at = models.DateTimeField('发布时间')  # 发布时间

    def __str__(self):
        return self.title  # 后台显示标题

    class Meta:
        verbose_name = '喃喃自语'
        verbose_name_plural = "喃喃自语"  # 类的复数
