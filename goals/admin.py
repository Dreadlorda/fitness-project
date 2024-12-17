from django.contrib import admin
from .models import Goal

@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'deadline', 'progress', 'created_at']
    list_filter = ['user', 'deadline']
    search_fields = ['title', 'description']
