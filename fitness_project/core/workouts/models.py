
from django.db import models
from django.contrib.auth.models import User

class Goal(models.Model):
    GOAL_TYPE_CHOICES = [
        ('steps', 'Steps per day'),
        ('calories', 'Calories burned'),
        ('visits', 'Gym visits per week')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='goals')
    goal_type = models.CharField(max_length=50, choices=GOAL_TYPE_CHOICES)
    target = models.PositiveIntegerField()
    progress = models.PositiveIntegerField(default=0)
    deadline = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.goal_type} - {self.target}'

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Badge Model
class Badge(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='badges/', null=True, blank=True)

    def __str__(self):
        return self.name

# Streak Tracking Model
class Streak(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='streak')
    current_streak = models.PositiveIntegerField(default=0)
    longest_streak = models.PositiveIntegerField(default=0)
    last_activity_date = models.DateField(null=True, blank=True)

    def update_streak(self):
        today = timezone.now().date()
        if self.last_activity_date == today:
            return  # Already counted today
        elif self.last_activity_date == today - timezone.timedelta(days=1):
            self.current_streak += 1
        else:
            self.current_streak = 1  # Reset streak if missed a day
        self.longest_streak = max(self.longest_streak, self.current_streak)
        self.last_activity_date = today
        self.save()

    def __str__(self):
        return f"{self.user.username}'s streak: {self.current_streak} days"

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    message = models.CharField(max_length=255)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.user.username}: {self.message}"

from django.db import models
from django.contrib.auth.models import User

class Achievement(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    awarded_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='achievements')
    awarded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# Adding indexing to commonly queried fields
class Meta:
    indexes = [
        models.Index(fields=['created_at']),
        models.Index(fields=['name']),
    ]
class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workouts')
    name = models.CharField(max_length=255)
    duration = models.PositiveIntegerField(help_text="Duration in minutes")
    calories_burned = models.PositiveIntegerField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name