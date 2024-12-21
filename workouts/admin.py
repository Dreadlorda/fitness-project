from django.contrib import admin
from .models import Workout

class WorkoutAdmin(admin.ModelAdmin):
    list_display = ['exercise_type', 'duration', 'date', 'user']  # Corrected fields
    list_filter = ['exercise_type', 'date']  # Removed invalid 'created_by'
    search_fields = ['exercise_type']

admin.site.register(Workout, WorkoutAdmin)
