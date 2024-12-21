
from django.apps import AppConfig

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        from django.contrib.auth.models import User
        from .models import UserProfile

        # Automatically create UserProfiles for users without one
        for user in User.objects.all():
            UserProfile.objects.get_or_create(user=user)
