from django.contrib import admin

from webapp.models import Comment, Technique, Category

admin.site.register(Comment)
admin.site.register(Technique)
admin.site.register(Category)
