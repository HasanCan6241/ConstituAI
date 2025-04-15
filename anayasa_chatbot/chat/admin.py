# chat/admin.py

from django.contrib import admin
from .models import Conversation, Message, Feedback


class MessageInline(admin.TabularInline):
    model = Message
    readonly_fields = ('sender', 'content', 'timestamp')
    extra = 0
    can_delete = False


class FeedbackInline(admin.TabularInline):
    model = Feedback
    readonly_fields = ('rating', 'comment', 'created_at')
    extra = 0
    can_delete = False


@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'session_id', 'created_at')
    search_fields = ('user__username', 'session_id')
    list_filter = ('created_at',)
    inlines = [MessageInline]


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'conversation', 'sender', 'short_content', 'timestamp')
    list_filter = ('sender', 'timestamp')
    search_fields = ('content',)
    inlines = [FeedbackInline]

    def short_content(self, obj):
        return obj.content[:50] + '...' if len(obj.content) > 50 else obj.content

    short_content.short_description = "İçerik"


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'message', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')