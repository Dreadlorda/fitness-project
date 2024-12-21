from django.contrib import admin
from goals.models import Goal
from nutrition.models import NutritionLog
from workouts.models import Workout
from users.models import UserProfile

@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ('title', 'due_date', 'is_completed', 'created_by')
    search_fields = ('title', 'created_by__username')
    list_filter = ('is_completed', 'due_date')

@admin.register(NutritionLog)
class NutritionLogAdmin(admin.ModelAdmin):
    list_display = ('meal', 'calories', 'date', 'user')
    search_fields = ('meal', 'user__username')
    list_filter = ('date',)

@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'duration', 'user')
    search_fields = ('name', 'user__username')
    list_filter = ('date',)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'join_date')
    search_fields = ('user__username', 'role')
    list_filter = ('role',)