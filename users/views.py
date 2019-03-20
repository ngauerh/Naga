from django.shortcuts import render

# Create your views here.
from .models import *
from blog.views import loadinfo


def aboutme(request):
    context = loadinfo()
    return render(request, 'about.html', context=context)


def ziyu(request):
    context = loadinfo()
    ziyu = Ziyu.objects.all()
    context['ziyu'] = ziyu
    return render(request, 'ziyu.html', context=context)