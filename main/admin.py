from django.contrib import admin
from .models import Questions

@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    """Questions"""
    list_display = ("name", "phoneNumber", "email", "service", "message")
