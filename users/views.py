from django.shortcuts import render

# Create your views here.
from .models import *
from blog.views import loadinfo


def aboutme(request):
    context = loadinfo()
    about = AboutMe.objects.all()
    context['about'] = about
    return render(request, 'about.html', context=context)