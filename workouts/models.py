
from django.db import models
from django.core.exceptions import ValidationError

def validate_positive(value):
    if value <= 0:
        raise ValidationError(f'{value} is not a positive number')

class Workout(models.Model):
    name = models.CharField(max_length=255)
    duration = models.PositiveIntegerField(validators=[validate_positive])  # Minutes
    calories_burned = models.PositiveIntegerField(validators=[validate_positive])  # Calories
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='workouts')

    def __str__(self):
        return self.name
