from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

class Workout(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='workouts')
    name = models.CharField(max_length=255)
    duration = models.PositiveIntegerField(help_text="Duration in minutes")
    calories_burned = models.PositiveIntegerField()
    date = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='created_workouts')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name