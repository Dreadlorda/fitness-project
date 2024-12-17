
from django.db import models
from django.contrib.auth.models import User

class ProgressLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    weight = models.FloatField(null=True, blank=True)
    workout_duration = models.PositiveIntegerField(null=True, blank=True)
    progress_photo = models.ImageField(upload_to="progress_photos/", null=Tr...
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Progress by {self.user.username} on {self.created_at.strfti...
