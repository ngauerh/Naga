from django.contrib import admin

# Register your models here.

from .models import *
# https://blog.csdn.net/xyw_blog/article/details/8951808
# https://www.cnblogs.com/wumingxiaoyao/p/6928297.html
# https://www.cnblogs.com/wumingxiaoyao/p/6928297.html
admin.site.site_header = "博客后台管理"   # 修改登陆界面标题
admin.site.site_title = "后台管理系统"


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'create_at', 'category')
    search_fields = ('title', 'author', "category__category")
    filter_horizontal = ('tags',)
    list_filter = ('tags', 'category', 'author')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'mid', 'message')


@admin.register(FriendlyLink)
class FriendlyLinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')


@admin.register(Siteinfo)
class SiteinfoAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon', 'pagesnum')


admin.site.register(Tag)
admin.site.register(Category)
