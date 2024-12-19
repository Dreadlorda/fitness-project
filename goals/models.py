from django.db import models
from django.conf import settings

class Goal(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    goal_type = models.CharField(max_length=50)
    target = models.FloatField()
    progress = models.FloatField()
    deadline = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
