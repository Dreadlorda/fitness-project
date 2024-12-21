from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from goals.models import Goal
from workouts.models import Workout

class AsyncAPITests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.client.login(username='testuser', password='password123')
        Goal.objects.create(user=self.user, title='Test Goal', description='A goal description', goal_type='Fitness', progress=50, target=100)
        Workout.objects.create(user=self.user, exercise_type='Running', sets=3, reps=10, duration=30, date='2025-01-01')

    def test_goal_api(self):
        response = self.client.get(reverse('async-goals-api'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('Test Goal', str(response.content))

    def test_workout_api(self):
        response = self.client.get(reverse('async-workouts-api'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('Running', str(response.content))
