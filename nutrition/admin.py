
from django.contrib import admin
from .models import NutritionLog

@admin.register(NutritionLog)
class NutritionLogAdmin(admin.ModelAdmin):
    list_display = ('food', 'calories', 'protein', 'carbs', 'fats', 'created_at')
    list_filter = ('calories', 'protein', 'carbs', 'fats')
    search_fields = ('food',)
    ordering = ('-created_at',)
