from django.contrib import admin

# Register your models here.
from .models import AboutMe


@admin.register(AboutMe)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('content',)
