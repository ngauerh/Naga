from django.shortcuts import render
from .models import *
from rest_framework import viewsets
from .serializers import BlogSerializer
# Create your views here.


# 首页
def index(request):
    blog = Blog.objects.all()
    context = {'blog_list': blog}
    return render(request, 'index.html', context)


# 详情页
def blog_details(request, bid):
    blog = Blog.objects.get(id=bid)
    context = {'blog_list': blog}
    message = Message.objects.filter(mid=int(bid)).order_by('-pk')
    context['message_list'] = message
    return render(request, 'details.html', context)
    # return render(request, 'base.html', context)


# 标签页
def tags(request):
    return render(request, 'tags.html')


# 分类页
def categories(request):
    return


class BlogAPI(viewsets.ModelViewSet):
    queryset = Blog.objects.all().order_by('-pk')
    serializer_class = BlogSerializer

