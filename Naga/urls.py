"""Naga URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from blog.views import page_not_found, permission_denied, page_error
try:
    from .settings import NAGA_ADMIN_PATH
except ImportError:
    NAGA_ADMIN_PATH = 'admin'

if len(NAGA_ADMIN_PATH) != 0:
    admin_prefix = r'^%s/' % NAGA_ADMIN_PATH
else:
    admin_prefix = r'^%s/' % 'admin'

handler403 = permission_denied
handler404 = page_not_found
handler500 = page_error

urlpatterns = [
    url(admin_prefix, admin.site.urls),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^u/', include('users.urls')),
    url(r'^', include('blog.urls')),
    url(r'^search/', include('haystack.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# http://www.shareditor.com/blogshow?blogId=134
