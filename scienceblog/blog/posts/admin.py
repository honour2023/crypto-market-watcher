# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Post


# Register your models here.

# class PostAdmin(admin.ModelAdmin):
#     list_display = ["title", "updated", "timestamp"]
#     list_display_links = ["updated"]
#     list_editable = ["title"]
#     search_fields = ["title", "content"]
#     list_filter = ["updated", "timestamp"]
#
#     class Meta:
#         Model = Post


admin.site.register(Post)
