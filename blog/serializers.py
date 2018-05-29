from .models import Blog
from django.contrib.auth.models import User
from rest_framework import serializers


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"
        # fields = ('title', 'content')
