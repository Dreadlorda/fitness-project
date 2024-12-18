
from django.contrib import admin
from .models import Achievement, Workout

@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_by', 'created_at')
    list_filter = ('created_at', 'created_by')
    search_fields = ('name', 'created_by__username')
    ordering = ('-created_at',)

@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('title', 'awarded_to', 'awarded_at')
    list_filter = ('awarded_at', 'awarded_to')
    search_fields = ('title', 'awarded_to__username')
    ordering = ('-awarded_at',)
