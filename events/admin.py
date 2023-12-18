from django.contrib import admin
from .models import EventPost, EventComment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(EventPost)
class EventPostAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'location', 'status', 'created_on')
    search_fields = ['title', 'description']
    list_filter = ('status', 'created_on')
    summernote_fields = ('description')


@admin.register(EventComment)
class EventCommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
