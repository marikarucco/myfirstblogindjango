from django.contrib import admin
from .models import Blog, Post, Comment


class BlogAdmin(admin.ModelAdmin):
    list_display = [
        'author',
        'title',
    ]


class PostAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'body',
    ]


class CommentAdmin(admin.ModelAdmin):
    list_display = [
        'author',
        'body',
    ]


admin.site.register(Blog, BlogAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
