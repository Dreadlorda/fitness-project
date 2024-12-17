
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

class CustomUser(AbstractUser):
    username = models.CharField(
        max_length=20,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z0-9_-]+$',
                message='Username can only contain letters, numbers, "-", an...
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
