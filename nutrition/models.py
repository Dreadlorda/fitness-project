from django.db import models
from django.conf import settings

class NutritionLog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    calories = models.PositiveIntegerField()
    protein = models.PositiveIntegerField(default=0)  # grams
    carbs = models.PositiveIntegerField(default=0)  # grams
    fat = models.PositiveIntegerField(default=0)  # grams
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.date}) - {self.calories} kcal"
