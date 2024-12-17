
from django.db import models
from django.contrib.auth.models import User
from .mixins import SlugMixin

class NutritionLog(models.Model, SlugMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    calories = models.PositiveIntegerField()
    slug = models.SlugField(unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.user.username})"
