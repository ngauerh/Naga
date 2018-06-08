from django.conf.urls import url, include
from .views import *
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'blog', BlogAPI)



handler403 = permission_denied
handler404 = page_not_found
handler500 = page_error

extra_pattern = [
    url(r'^details/(?P<bid>[0-9]+)$', blog_details, name='details'),
    url(r'^tags$', tags, name='tags'),
    url(r'^categories$', categories, name='categories'),
    url(r'^archives$', archives, name='archives'),
    url(r'^comment$', comment, name='comment'),
    url(r'^blogtags$', blogtags, name='blogtags'),
]


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^b/', include(extra_pattern)),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]