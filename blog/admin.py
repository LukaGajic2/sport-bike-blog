from django.contrib import admin
from .models import BlogPost, BlogComment
from django_summernote.admin import SummernoteModelAdmin

# Class used from "I think therefore I blog" walkthrough.


@admin.register(BlogPost)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

# Class used from "I think therefore I blog" walkthrough.


@admin.register(BlogComment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    """
    Function to approve pending
    user comments on blog posts
    """

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
