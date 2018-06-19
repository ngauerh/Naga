from django.conf.urls import url, include
from .views import *


extra_pattern = [
    # url(r'^details/(?P<bid>[0-9]+)$', blog_details, name='details'),
    # url(r'^tags$', tags, name='tags'),
]


urlpatterns = [
    url(r'^$', aboutme, name='aboutme'),

]

