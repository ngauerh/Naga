from django.db import OperationalError
from django.shortcuts import render
from .models import *
from users.models import AboutMe
from rest_framework import viewsets
from .serializers import BlogSerializer
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from urllib.parse import urljoin
from django.shortcuts import redirect, get_object_or_404
from django.contrib.syndication.views import Feed
from django.db.models.aggregates import Count
from haystack.views import SearchView
from django.utils.feedgenerator import Rss201rev2Feed
from Naga.settings import NAGA_WEB_URL


# 公共的侧边栏信息
def loadinfo():
    context = {}
    link = FriendlyLink.objects.all()
    info = Siteinfo.objects.first()
    context['link_list'] = link
    context['info'] = info
    a = AboutMe.objects.first()
    context['about'] = a
    tag_yun = Tag.objects.annotate(num_post=Count('blog'))
    context['tag_yun'] = tag_yun
    adsense = Adsense.objects.all()
    context['ad_list'] = adsense
    return context


# 首页
def index(request):
    context = loadinfo()
    blog_list = Blog.objects.all()
    try:
        paginator = Paginator(blog_list, context['info'].pagesnum)
    except AttributeError:
        paginator = Paginator(blog_list, 8)

    page = request.GET.get('page')
    if page:
        b_list = paginator.page(page).object_list
    else:
        b_list = paginator.page(1).object_list
    try:
        customer = paginator.page(page)
    except PageNotAnInteger:
        customer = paginator.page(1)
    except EmptyPage:
        customer = paginator.page(paginator.num_pages)

    commend = Blog.objects.filter(topped=True).all().values('title', 'id')
    commend = list(commend)
    context['commend_list'] = commend
    context['cus_list'] = customer
    context['blog_list'] = b_list

    return render(request, 'index.html', context)


# 详情页
def blog_details(request, bid):
    context = loadinfo()
    try:
        blog = Blog.objects.get(title=bid)
        context['blog_list'] = blog
        message = Message.objects.filter(mid=blog.id).order_by('-pk')
        context['message_list'] = message
        tag = blog.tags.all()
        context['tag_list'] = tag

        # 上一篇，下一篇
        context['previous_blog'] = Blog.objects.get(id=blog.id-1)
        context['next_blog'] = Blog.objects.get(id=blog.id+1)

        response = render(request, 'details.html', context)

        if not request.COOKIES.get('blog_{}_readed'.format(str(blog.id))):
            blog.views += 1
            blog.save()
            response.set_cookie('blog_{}_readed'.format(str(blog.id)), 'read', max_age=600)
        return response
    except:
        return render(request, 'error/404.html')


# 标签页
def tags(request):
    context = loadinfo()
    tag = Tag.objects.annotate(num_post=Count('blog'))
    context['tag_list'] = tag
    return render(request, 'tags.html', context=context)


def blogtags(request):
    context = loadinfo()
    tid = request.GET.get('tid')
    blog = Blog.objects.filter(tags=tid)
    context['blog_list'] = blog

    return render(request, 'result.html', context=context)


# 分类页
def categories(request):
    context = loadinfo()
    category = Category.objects.annotate(num_post=Count('blog'))
    context['ca_list'] = category
    return render(request, 'tags.html', context=context)


# 归档
def archives(request):
    context = loadinfo()
    dates = Blog.objects.datetimes('create_at', 'month', order='DESC')
    context['dates'] = dates
    blog_list = Blog.objects.all().order_by('-create_at')
    total = Blog.objects.all().count()
    context['total'] = total
    context['blog_list'] = blog_list
    return render(request, 'archives.html', context=context)


# 评论
def comment(request):
    try:
        ob = Message()
        ob.mid = get_object_or_404(Blog, pk=request.POST['bid'])
        ob.name = request.POST["username"]
        ob.email = request.POST["email"]
        ob.message = request.POST['message']
        ob.save()
        url = urljoin('/b/details/', request.POST["bid"])
        return redirect(url)
    except:
        url = urljoin('/b/details/', request.POST["bid"])
        return redirect(url)


# api接口
class BlogAPI(viewsets.ModelViewSet):
    queryset = Blog.objects.all().order_by('-pk')
    serializer_class = BlogSerializer


# RSS
class RssFeed(Feed):
    feed_type = Rss201rev2Feed
    try:
        description = Siteinfo.objects.first().title if Siteinfo.objects.first() else '无标题'
        title = Siteinfo.objects.first().title if Siteinfo.objects.first() else '无标题'
    except OperationalError:
        description = '无标题'
        title = '无标题'
    feed_url = urljoin(NAGA_WEB_URL, 'feed')
    link = NAGA_WEB_URL

    def items(self):
        return Blog.objects.all().order_by('-update_at')

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.summary

    def item_link(self, item):
        return item.get_absolute_url()


class QSearchView(SearchView):
    def extra_context(self):       # 重载extra_context来添加额外的context内容
        context = super(QSearchView, self).extra_context()
        link = FriendlyLink.objects.all()
        info = Siteinfo.objects.first()
        context['link_list'] = link
        context['info'] = info
        a = AboutMe.objects.first()
        context['about'] = a
        tag_yun = Tag.objects.annotate(num_post=Count('blog'))
        context['tag_yun'] = tag_yun
        adsense = Adsense.objects.all()
        context['ad_list'] = adsense
        return context


# 异常
def page_not_found(request):
    return render(request, 'error/404.html')


def page_error(request):
    return render(request, 'error/500.html')


def permission_denied(request):
    return render(request, 'error/403.html')
