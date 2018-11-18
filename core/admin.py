from django.contrib import admin

from .models import BlogData, Website

admin.site.register(Website)
admin.site.register(BlogData)