from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model


class CustomUser(AbstractUser):
    username = models.CharField(
        max_length=20,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z0-9_-]+$',
                message='Username can only contain letters, numbers, "-", and "_".',
                code='invalid_username'
            )
        ],
    )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.PositiveIntegerField(null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    enable_notifications = models.BooleanField(default=False)
    daily_calorie_goal = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.user.username} Profile'


# Badge Model
class Badge(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='badges/', null=True, blank=True)

    def __str__(self):
        return self.name


# Streak Tracking Model
class Streak(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='streak')
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
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='notifications')
    message = models.CharField(max_length=255)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.user.username}: {self.message}"


class Achievement(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    awarded_to = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='achievements')
    awarded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

@receiver(post_save, sender=get_user_model())
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
