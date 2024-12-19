from django.db import models
from django.conf import settings

class NutritionLog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    calories = models.PositiveIntegerField()
    protein = models.PositiveIntegerField(default=0)
    carbs = models.PositiveIntegerField(default=0)
    fat = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

class ProgressLog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='progress_logs')
    nutrition_log = models.ForeignKey(NutritionLog, on_delete=models.CASCADE, related_name='progress_logs')
    progress = models.PositiveIntegerField(help_text="Track the user's progress (e.g., calorie intake)")
    date = models.DateField(auto_now_add=True)
    notes = models.TextField(null=True, blank=True)
