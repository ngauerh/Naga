from django.contrib import admin

# Register your models here.
from .models import AboutMe, Ziyu


@admin.register(AboutMe)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('content',)


@admin.register(Ziyu)
class ZiyuAdmin(admin.ModelAdmin):
    list_display = ('content',)
