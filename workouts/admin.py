
from django.contrib import admin
from .models import Workout

@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('name', 'duration', 'calories_burned', 'created_at')
    list_filter = ('duration', 'calories_burned')
    search_fields = ('name',)
    ordering = ('-created_at',)
