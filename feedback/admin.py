from django.contrib import admin

from .models import Feedback


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):

    """Админ-панель в модели профиля"""
    list_display = ("email", "ip_address", "user", "content")
    list_display_links = ('email', 'ip_address')
