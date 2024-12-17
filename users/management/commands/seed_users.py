
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Seed the database with example users'

    def handle(self, *args, **kwargs):
        users_data = [
            {'username': 'admin', 'email': 'admin@example.com', 'password': ...
            {'username': 'staff', 'email': 'staff@example.com', 'password': ...
            {'username': 'user1', 'email': 'user1@example.com', 'password': ...
            {'username': 'user2', 'email': 'user2@example.com', 'password': ...
        ]

        for user_data in users_data:
            if not User.objects.filter(username=user_data['username']).exist...
                user = User.objects.create_user(
                    username=user_data['username'],
                    email=user_data['email'],
                    password=user_data['password']
                )
                user.is_staff = user_data['is_staff']
                user.is_superuser = user_data['is_superuser']
                user.save()
                self.stdout.write(f"User {user_data['username']} created suc...
            else:
                self.stdout.write(f"User {user_data['username']} already exi...
