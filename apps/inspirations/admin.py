from django.contrib import admin

from apps.inspirations.models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['created_at', 'author', 'message']
    search_fields = ['author', 'message']
