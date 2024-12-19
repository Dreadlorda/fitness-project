from django.contrib import admin
from .models import Workout

@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_by', 'created_at')
    list_filter = ('created_at', 'created_by')
    search_fields = ('name', 'created_by__username')
    ordering = ('-created_at',)
