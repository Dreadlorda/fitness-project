from django.db import models
from django.conf import settings

class Goal(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    goal_type = models.CharField(max_length=50, choices=[
        ('Fitness', 'Fitness'),
        ('Education', 'Education'),
        ('Career', 'Career'),
    ])
    target = models.FloatField()
    progress = models.FloatField(default=0.0)
    deadline = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.goal_type}) - {self.progress}/{self.target}"
