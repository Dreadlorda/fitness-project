from django.db import models
from django.contrib.auth.models import User

class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    goal_type = models.CharField(max_length=50)  # Add this field
    target = models.FloatField()  # Add this field
    progress = models.FloatField()
    deadline = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
