from django.conf.urls import url, include
from .views import *
app_name = 'users'

urlpatterns = [
    url(r'^about$', aboutme, name='aboutme'),
    url(r'^ziyu$', ziyu, name='ziyu'),

]

